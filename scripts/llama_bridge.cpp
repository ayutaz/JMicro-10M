// Native, token-ID-first llama.cpp bridge. Request/response JSON on disk keeps
// the Python codec authoritative. Logits are native FP32 little-endian files.
#include "llama.h"
#include "json.hpp"
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <algorithm>
using json = nlohmann::json;

int main(int argc, char **argv) {
    try {
        if (argc != 4) throw std::runtime_error("usage: bridge model.gguf request.json response.json");
        json request;
        std::ifstream(argv[2]) >> request;
        llama_backend_init();
        auto mp = llama_model_default_params();
        mp.n_gpu_layers = 0;
        auto *model = llama_model_load_from_file(argv[1], mp);
        if (!model) throw std::runtime_error("model load failed");
        const auto *vocab = llama_model_get_vocab(model);
        int nv = llama_vocab_n_tokens(vocab);
        json response = {{"vocab_size", nv}, {"native_eot_is_eog", llama_vocab_is_eog(vocab, 7)},
                         {"native_eos_is_eog", llama_vocab_is_eog(vocab, 3)}};
        auto cp = llama_context_default_params();
        cp.n_ctx = 1024; cp.n_batch = 1024; cp.n_ubatch = 1024;
        cp.n_threads = 2; cp.n_threads_batch = 2;
        cp.type_k = GGML_TYPE_F32; cp.type_v = GGML_TYPE_F32;
        cp.flash_attn_type = LLAMA_FLASH_ATTN_TYPE_DISABLED;
        auto *ctx = llama_init_from_model(model, cp);
        if (!ctx) throw std::runtime_error("context creation failed");
        if (request.contains("tokenize")) {
            response["tokenize"] = json::array();
            for (const auto &item : request["tokenize"]) {
                std::string text = item.get<std::string>();
                std::vector<llama_token> ids(text.size() * 4 + 32);
                int n = llama_tokenize(vocab, text.data(), text.size(), ids.data(), ids.size(), false, false);
                if (n < 0) throw std::runtime_error("tokenize failed");
                ids.resize(n);
                std::vector<char> decoded(text.size() * 8 + 128);
                int d = llama_detokenize(vocab, ids.data(), n, decoded.data(), decoded.size(), true, false);
                if (d < 0) throw std::runtime_error("detokenize failed");
                response["tokenize"].push_back({{"ids", ids}, {"decoded", std::string(decoded.data(), d)}});
            }
        }
        auto decode = [&](const std::vector<llama_token> &ids, int position, bool all_logits) {
            if (ids.empty() || position + ids.size() > 1024) throw std::runtime_error("context limit");
            auto batch = llama_batch_init(ids.size(), 0, 1);
            batch.n_tokens = ids.size();
            for (int i = 0; i < batch.n_tokens; ++i) {
                if (ids[i] < 0 || ids[i] >= nv) throw std::runtime_error("ID outside vocabulary");
                batch.token[i] = ids[i]; batch.pos[i] = position + i;
                batch.n_seq_id[i] = 1; batch.seq_id[i][0] = 0;
                batch.logits[i] = all_logits || i == batch.n_tokens - 1;
            }
            int status = llama_decode(ctx, batch);
            llama_batch_free(batch);
            if (status != 0) throw std::runtime_error("llama_decode failed: " + std::to_string(status));
        };
        if (request.contains("runs")) {
            response["runs"] = json::array();
            for (const auto &run : request["runs"]) {
                llama_memory_clear(llama_get_memory(ctx), true);
                std::ofstream output(run["logits_file"].get<std::string>(), std::ios::binary);
                int position = 0;
                for (const auto &chunk : run["chunks"]) {
                    auto ids = chunk.get<std::vector<llama_token>>();
                    decode(ids, position, true);
                    for (int i = 0; i < (int)ids.size(); ++i) {
                        const float *logits = llama_get_logits_ith(ctx, i);
                        if (!logits) throw std::runtime_error("missing logits");
                        output.write(reinterpret_cast<const char *>(logits), nv * sizeof(float));
                    }
                    position += ids.size();
                }
                if (!output.good()) throw std::runtime_error("could not write logits");
                response["runs"].push_back({{"tokens", position}, {"logits_file", run["logits_file"]}});
            }
        }
        if (request.contains("generate")) {
            llama_memory_clear(llama_get_memory(ctx), true);
            auto ids = request["generate"]["input_ids"].get<std::vector<llama_token>>();
            int limit = request["generate"].value("max_new_tokens", 16);
            auto stops = request["generate"].value("stop_ids", std::vector<int>{7, 3});
            auto suppress = request["generate"].value("suppress_ids", std::vector<int>{0,1,2,4,5,6});
            if ((int)ids.size() + limit > 1024 || limit <= 0) throw std::runtime_error("invalid generation budget");
            decode(ids, 0, false);
            std::vector<int> generated;
            std::string reason = "max_new_tokens";
            int pos = ids.size();
            for (int step = 0; step < limit; ++step) {
                float *logits = llama_get_logits_ith(ctx, -1);
                for (int i : suppress) logits[i] = -INFINITY;
                int next = std::max_element(logits, logits + nv) - logits;
                // Explicit hook tests the stop controller; separate synthetic
                // weight fixtures verify actual native argmax selects EOT/EOS.
                if (step == 0 && request["generate"].contains("forced_first_id"))
                    next = request["generate"]["forced_first_id"].get<int>();
                generated.push_back(next);
                if (std::find(stops.begin(), stops.end(), next) != stops.end()) {
                    reason = "stop_id"; break;
                }
                if (step + 1 < limit) decode({next}, pos++, false);
            }
            response["generation"] = {{"ids", generated}, {"stop_reason", reason}};
        }
        std::ofstream(argv[3]) << response.dump(2) << "\n";
        llama_free(ctx); llama_model_free(model); llama_backend_free();
    } catch (const std::exception &e) { std::cerr << e.what() << "\n"; return 1; }
    return 0;
}
