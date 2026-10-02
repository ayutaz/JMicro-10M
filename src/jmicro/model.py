"""JMicro decoder: shared-head QK RMSNorm, half-split RoPE, GQA, tied output.

Cache stores post-normalization/post-RoPE K and unrotated V. Positions count
valid tokens per sequence, while physical padding slots remain masked. Chunk
attention uses absolute positions, never a square causal mask on a rectangle.
"""
from dataclasses import dataclass
from pathlib import Path
import json

import torch
from torch import nn
from torch.nn import functional as F
from safetensors.torch import save_file, load_file


class RMSNorm(nn.Module):
    def __init__(self, size: int, eps: float):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(size))
        self.eps = eps

    def forward(self, x):
        normalized = x.float() * torch.rsqrt(x.float().square().mean(-1, keepdim=True) + self.eps)
        return normalized.to(x.dtype) * self.weight


def rope(x, positions, theta):
    dim = x.shape[-1]
    with torch.autocast(device_type=x.device.type, enabled=False):
        inv = 1.0 / (theta ** (torch.arange(0, dim, 2, device=x.device).float() / dim))
        phase = positions.float()[..., None] * inv
        phase = torch.cat((phase, phase), dim=-1)[:, None]
        cos, sin = phase.cos().to(x.dtype), phase.sin().to(x.dtype)
    half = dim // 2
    rotated = torch.cat((-x[..., half:], x[..., :half]), dim=-1)
    return x * cos + rotated * sin


@dataclass
class KVCache:
    layers: list[tuple[torch.Tensor, torch.Tensor]]
    valid: torch.Tensor
    positions: torch.Tensor


@dataclass
class ModelOutput:
    logits: torch.Tensor
    cache: KVCache | None = None
    loss: torch.Tensor | None = None


class Attention(nn.Module):
    def __init__(self, config):
        super().__init__()
        h, d = config["hidden_size"], config["head_dim"]
        self.qheads = config["num_attention_heads"]
        self.kvheads = config["num_key_value_heads"]
        self.dim, self.theta, self.scale = d, config["rope_theta"], config["attention_scale"]
        self.q_proj = nn.Linear(h, self.qheads * d, bias=False)
        self.k_proj = nn.Linear(h, self.kvheads * d, bias=False)
        self.v_proj = nn.Linear(h, self.kvheads * d, bias=False)
        self.o_proj = nn.Linear(self.qheads * d, h, bias=False)
        self.q_norm = RMSNorm(d, config["rms_norm_eps"])
        self.k_norm = RMSNorm(d, config["rms_norm_eps"])

    def forward(self, x, positions, allowed, past):
        batch, length, _ = x.shape
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = project(self.v_proj, self.kvheads)
        if past is not None:
            k, v = torch.cat((past[0], k), dim=2), torch.cat((past[1], v), dim=2)
        # Explicit repeats keep mapping contiguous: Q heads 0/1->KV0, 2/3->KV1.
        groups = self.qheads // self.kvheads
        attended = F.scaled_dot_product_attention(q, k.repeat_interleave(groups, dim=1),
            v.repeat_interleave(groups, dim=1), attn_mask=allowed[:, None],
            dropout_p=0.0, is_causal=False, scale=self.scale)
        attended = attended.transpose(1, 2).reshape(batch, length, -1)
        return self.o_proj(attended), (k, v)


class MLP(nn.Module):
    def __init__(self, config):
        super().__init__()
        h, f = config["hidden_size"], config["intermediate_size"]
        self.gate_proj = nn.Linear(h, f, bias=False)
        self.up_proj = nn.Linear(h, f, bias=False)
        self.down_proj = nn.Linear(f, h, bias=False)

    def forward(self, x):
        return self.down_proj(F.silu(self.gate_proj(x)) * self.up_proj(x))


class Block(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.self_attn = Attention(config)
        self.mlp = MLP(config)
        self.input_layernorm = RMSNorm(config["hidden_size"], config["rms_norm_eps"])
        self.post_attention_layernorm = RMSNorm(config["hidden_size"], config["rms_norm_eps"])

    def forward(self, x, positions, allowed, past):
        attention, cache = self.self_attn(self.input_layernorm(x), positions, allowed, past)
        x = x + attention
        return x + self.mlp(self.post_attention_layernorm(x)), cache


class Decoder(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.embed_tokens = nn.Embedding(config["vocab_size"], config["hidden_size"])
        self.layers = nn.ModuleList([Block(config) for _ in range(config["num_hidden_layers"])])
        self.norm = RMSNorm(config["hidden_size"], config["rms_norm_eps"])


class JMicroModel(nn.Module):
    def __init__(self, config: dict):
        super().__init__()
        self.config = dict(config)
        if not (config["tie_word_embeddings"] and config["rope_layout"] == "half_split" and
                config["qk_norm_type"] == "rms_head_shared" and config["qk_norm_before_rope"] and
                config["rotary_dim"] == config["head_dim"] and config["activation"] == "swiglu" and
                not config["attention_bias"] and not config["mlp_bias"] and config["dropout"] == 0):
            raise ValueError("Unsupported architecture contract")
        if config["hidden_size"] != config["num_attention_heads"] * config["head_dim"] or config["num_attention_heads"] % config["num_key_value_heads"]:
            raise ValueError("Invalid GQA dimensions")
        self.model = Decoder(config)
        self.lm_head = nn.Linear(config["hidden_size"], config["vocab_size"], bias=False)
        self.lm_head.weight = self.model.embed_tokens.weight
        self.apply(self._initialize)

    def _initialize(self, module):
        if isinstance(module, (nn.Linear, nn.Embedding)):
            nn.init.normal_(module.weight, mean=0, std=self.config["initializer_std"])
        elif isinstance(module, RMSNorm):
            nn.init.constant_(module.weight, self.config["norm_initial_gain"])

    def forward(self, input_ids, attention_mask=None, cache=None, use_cache=False, labels=None):
        if input_ids.ndim != 2 or input_ids.shape[1] == 0:
            raise ValueError("Expected nonempty [batch, tokens] IDs")
        valid = torch.ones_like(input_ids, dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError("Mask must match current IDs (including chunk decode)")
        if cache is not None:
            if len(cache.layers) != len(self.model.layers) or cache.valid.shape[0] != input_ids.shape[0]:
                raise ValueError("Cache batch/layer mismatch")
            if cache.valid.device != input_ids.device:
                raise ValueError("Cache and input devices differ")
            before = cache.valid.sum(-1)
        else:
            before = torch.zeros(input_ids.shape[0], device=input_ids.device, dtype=torch.long)
        positions = (before[:, None] + valid.long().cumsum(-1) - 1).clamp_min(0)
        if ((before + valid.sum(-1)) > self.config["max_position_embeddings"]).any():
            raise ValueError("Context exceeded: truncate complete turns and reprefill")
        key_valid = valid if cache is None else torch.cat((cache.valid, valid), dim=1)
        key_positions = positions if cache is None else torch.cat((cache.positions, positions), dim=1)
        allowed = valid[:, :, None] & key_valid[:, None, :] & (key_positions[:, None, :] <= positions[:, :, None])
        x, layers = self.model.embed_tokens(input_ids), []
        for index, block in enumerate(self.model.layers):
            x, kv = block(x, positions, allowed, None if cache is None else cache.layers[index])
            layers.append(kv)
        logits = self.lm_head(self.model.norm(x)).float() * valid[..., None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape:
                raise ValueError("Labels require full current sequence")
            if labels[:, 1:].ne(-100).any():
                loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]), labels[:, 1:].reshape(-1), ignore_index=-100)
            else:
                raise ValueError("No supervised targets after shifting")
        return ModelOutput(logits, KVCache(layers, key_valid, key_positions) if use_cache else None, loss)

    def save(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "jmicro_config.json").write_text(json.dumps(self.config, indent=2) + "\n")
        save_file({k: v.detach().contiguous() for k, v in self.state_dict().items() if k != "lm_head.weight"}, str(directory / "model.safetensors"))

    @classmethod
    def load(cls, directory: Path):
        model = cls(json.loads((directory / "jmicro_config.json").read_text()))
        result = model.load_state_dict(load_file(str(directory / "model.safetensors")), strict=False)
        if result.missing_keys != ["lm_head.weight"] or result.unexpected_keys:
            raise ValueError(f"Weight contract mismatch: {result}")
        return model

    def hf_reference(self):
        from transformers import Qwen3Config, Qwen3ForCausalLM
        c = self.config
        config = Qwen3Config(vocab_size=c["vocab_size"], hidden_size=c["hidden_size"],
            intermediate_size=c["intermediate_size"], num_hidden_layers=c["num_hidden_layers"],
            num_attention_heads=c["num_attention_heads"], num_key_value_heads=c["num_key_value_heads"],
            head_dim=c["head_dim"], hidden_act="silu", max_position_embeddings=c["max_position_embeddings"],
            initializer_range=c["initializer_std"], rms_norm_eps=c["rms_norm_eps"], tie_word_embeddings=True,
            rope_parameters={"rope_type": "default", "rope_theta": c["rope_theta"]},
            attention_bias=False, attention_dropout=0.0, pad_token_id=0, bos_token_id=2, eos_token_id=3)
        config._attn_implementation = "eager"
        reference = Qwen3ForCausalLM(config).eval()
        reference.load_state_dict(self.state_dict(), strict=True)
        return reference
