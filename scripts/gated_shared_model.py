"""Native unique blocks, each followed by a zero-gated reuse of both residuals.

This is an experimental combination of immediate block sharing and zero gates,
not an exact MobileLLM/ReZero replication. Each logical invocation has its own
KV cache even though both invocations use the same parameters.
"""
import copy
import torch
from torch import nn
from torch.nn import functional as F
from jmicro.model import JMicroModel, ModelOutput, KVCache

POLICY = dict(kind='immediate_shared_second_invocation_zero_residual_gate_v1',
              invocations_per_unique_block=2, initial_gate=0.,
              gate_sharing='one_scalar_per_unique_block_shared_by_second_attention_and_MLP',
              cache='separate_per_logical_invocation', gates_trainable=True)


class GatedSharedModel(JMicroModel):
    def __init__(self, config):
        if config.get('gated_shared_reuse') != POLICY:
            raise ValueError('Explicit frozen gated-sharing config required')
        native = {k: v for k, v in config.items() if k != 'gated_shared_reuse'}
        super().__init__(native)
        self.config = copy.deepcopy(config)
        self.reuse_gates = nn.Parameter(torch.zeros(native['num_hidden_layers']))

    @classmethod
    def from_native(cls, native):
        if isinstance(native, cls) or 'gated_shared_reuse' in native.config:
            raise ValueError('Unmodified native parent required')
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result.config = dict(copy.deepcopy(native.config), gated_shared_reuse=copy.deepcopy(POLICY))
        # Transfer exact objects, preserving native optimizer references and ties.
        result.model, result.lm_head = native.model, native.lm_head
        result.reuse_gates = nn.Parameter(torch.zeros(len(native.model.layers),
            device=native.model.embed_tokens.weight.device, dtype=torch.float32))
        result.train(native.training)
        return result

    @property
    def logical_layers(self):
        return 2*len(self.model.layers)

    def reused_block(self, block, index, x, positions, allowed, past, causal=False):
        gate = self.reuse_gates[index].to(x.dtype)
        attention, cache = block.self_attn(block.input_layernorm(x), positions, allowed, past, causal)
        x = x + gate*attention
        return x + gate*block.mlp(block.post_attention_layernorm(x)), cache

    def forward(self, input_ids, attention_mask=None, cache=None, use_cache=False,
                labels=None, training_fast_path=False):
        if input_ids.ndim != 2 or input_ids.shape[1] == 0:
            raise ValueError('Expected nonempty [batch,tokens] IDs')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Fast training requires unpadded blocks without cache/labels')
            if input_ids.shape[1] > self.config['max_position_embeddings']:
                raise ValueError('Training context exceeds model')
            positions = torch.arange(input_ids.shape[1], device=input_ids.device)[None].expand(input_ids.shape[0], -1)
            x = self.model.embed_tokens(input_ids)
            for index, block in enumerate(self.model.layers):
                x, _ = block(x, positions, None, None, causal=True)
                x, _ = self.reused_block(block, index, x, positions, None, None, causal=True)
            return ModelOutput(self.lm_head(self.model.norm(x)).float())
        valid = torch.ones_like(input_ids, dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Mask must match current IDs')
        if cache is not None:
            if len(cache.layers) != self.logical_layers or cache.valid.shape[0] != input_ids.shape[0]:
                raise ValueError('Cache batch/logical-layer mismatch')
            if cache.valid.device != input_ids.device:
                raise ValueError('Cache/input devices differ')
            before = cache.valid.sum(-1)
        else:
            before = torch.zeros(input_ids.shape[0], device=input_ids.device, dtype=torch.long)
        positions = (before[:, None]+valid.long().cumsum(-1)-1).clamp_min(0)
        if ((before+valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded: truncate complete turns and reprefill')
        key_valid = valid if cache is None else torch.cat((cache.valid, valid), dim=1)
        key_positions = positions if cache is None else torch.cat((cache.positions, positions), dim=1)
        allowed = valid[:, :, None] & key_valid[:, None, :] & (key_positions[:, None, :] <= positions[:, :, None])
        x, layers = self.model.embed_tokens(input_ids), []
        for index, block in enumerate(self.model.layers):
            x, kv = block(x, positions, allowed, None if cache is None else cache.layers[2*index])
            layers.append(kv)
            x, kv = self.reused_block(block, index, x, positions, allowed,
                                     None if cache is None else cache.layers[2*index+1])
            layers.append(kv)
        logits = self.lm_head(self.model.norm(x)).float()*valid[..., None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape:
                raise ValueError('Labels require full current sequence')
            if not labels[:, 1:].ne(-100).any():
                raise ValueError('No supervised targets after shifting')
            loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]),
                                   labels[:, 1:].reshape(-1), ignore_index=-100)
        return ModelOutput(logits, KVCache(layers, key_valid, key_positions) if use_cache else None, loss)

    def hf_reference(self):
        raise ValueError('Gated shared architecture requires a dedicated export adapter; stock Llama cannot silently load it')
