"""Write HF and float GGUF artifacts without changing model or tokenizer IDs."""
from pathlib import Path
import shutil

import gguf
from safetensors.torch import load_file

from jmicro.experiment import write_json, sha256
from jmicro.tokenizer import Tokenizer, CODEC_VERSION

CHAT_TEMPLATE = "{{ bos_token }}{% for message in messages %}{{ '<|' + message['role'] + '|>' }}{{ message['content'] }}{{ '<|eot|>' }}{% endfor %}{% if add_generation_prompt %}{{ '<|assistant|>' }}{% endif %}"


def export_hf(model, tokenizer_path: Path, directory: Path):
    reference = model.hf_reference()
    reference.save_pretrained(directory, safe_serialization=True)
    write_json(directory / "jmicro_config.json", model.config)
    shutil.copyfile(tokenizer_path, directory / "tokenizer.model")
    tok = Tokenizer(directory / "tokenizer.model")
    tok.save_wrapper(directory)
    write_json(directory / "artifact_manifest.json", {"tokenizer_sha256": sha256(tok.path),
               "weights_sha256": sha256(directory / "model.safetensors"), "codec": CODEC_VERSION})
    write_json(directory / "special_tokens.json", [{"id": i, "piece": tok.sp.id_to_piece(i)} for i in range(8)])
    # The template documents the rendered format. The body codec inserts IDs;
    # encoding this rendered string would violate literal-role handling.
    (directory / "chat_template.jinja").write_text(CHAT_TEMPLATE + "\n")
    write_json(directory / "generation_config.json", {"bos_token_id": 2, "pad_token_id": 0,
        "eos_token_id": [7, 3], "suppress_tokens": [0, 1, 2, 4, 5, 6], "max_new_tokens": 64,
        "do_sample": False})
    return reference


def llama_rope_rows(tensor, heads):
    """Half-split HF Q/K rows -> interleaved llama.cpp Llama RoPE rows."""
    rows, columns = tensor.shape
    if rows % (2 * heads):
        raise ValueError("Q/K rows must contain complete even-sized heads")
    return tensor.reshape(heads, 2, rows // heads // 2, columns).transpose(1, 2).reshape(rows, columns).contiguous()


def export_gguf(hf_directory: Path, path: Path, config: dict):
    """HF safetensors -> Qwen3 (QK-Norm) or Llama (NoNorm) FP32 GGUF.

    Qwen3 GGML RoPE uses half-split (NEOX); Q/K weights need no permutation.
    Built-in SPM is measured separately; external SentencePiece is normative.
    """
    tok = Tokenizer(hf_directory / "tokenizer.model")
    no_qk_norm = config["qk_norm_type"] == "none"
    architecture = "llama" if no_qk_norm else "qwen3"
    writer = gguf.GGUFWriter(path, architecture)
    writer.add_name(config["name"] if no_qk_norm else config["name"] + "-random-seed42")
    writer.add_context_length(config["max_position_embeddings"])
    writer.add_embedding_length(config["hidden_size"])
    writer.add_block_count(config["num_hidden_layers"])
    writer.add_feed_forward_length(config["intermediate_size"])
    writer.add_head_count(config["num_attention_heads"])
    writer.add_head_count_kv(config["num_key_value_heads"])
    writer.add_key_length(config["head_dim"])
    writer.add_value_length(config["head_dim"])
    writer.add_rope_dimension_count(config["rotary_dim"])
    writer.add_rope_freq_base(config["rope_theta"])
    writer.add_layer_norm_rms_eps(config["rms_norm_eps"])
    writer.add_file_type(gguf.LlamaFileType.ALL_F32)
    writer.add_tokenizer_model("llama")
    writer.add_token_list([tok.sp.id_to_piece(i) for i in range(tok.vocab_size)])
    writer.add_token_scores([tok.sp.get_score(i) for i in range(tok.vocab_size)])
    writer.add_token_types([2 if tok.sp.is_unknown(i) else 3 if tok.sp.is_control(i) else
                            6 if tok.sp.is_byte(i) else 1 for i in range(tok.vocab_size)])
    writer.add_bos_token_id(2)
    writer.add_eos_token_id(3)
    writer.add_eot_token_id(7)
    writer.add_unk_token_id(1)
    writer.add_pad_token_id(0)
    writer.add_add_bos_token(False)
    writer.add_add_eos_token(False)
    writer.add_add_space_prefix(False)
    writer.add_remove_extra_whitespaces(False)
    writer.add_string("jmicro.external_codec", CODEC_VERSION)
    writer.add_string("jmicro.tokenizer_sha256", sha256(tok.path))
    writer.add_bool("jmicro.external_tokenizer_required", True)
    writer.add_chat_template(CHAT_TEMPLATE)
    mapping = gguf.get_tensor_name_map(gguf.MODEL_ARCH.LLAMA if no_qk_norm else gguf.MODEL_ARCH.QWEN3, config["num_hidden_layers"])
    state = load_file(str(hf_directory / "model.safetensors"))
    names = {}
    for name, tensor in state.items():
        if name == "lm_head.weight":
            continue
        if no_qk_norm and name.endswith("self_attn.q_proj.weight"):
            tensor = llama_rope_rows(tensor, config["num_attention_heads"])
        elif no_qk_norm and name.endswith("self_attn.k_proj.weight"):
            tensor = llama_rope_rows(tensor, config["num_key_value_heads"])
        mapped = mapping.get_name(name, try_suffixes=(".weight",))
        if mapped is None:
            raise ValueError(f"Unmapped HF tensor: {name}")
        writer.add_tensor(mapped, tensor.float().numpy())
        names[name] = mapped
    writer.write_header_to_file()
    writer.write_kv_data_to_file()
    writer.write_tensors_to_file()
    writer.close()
    return names
