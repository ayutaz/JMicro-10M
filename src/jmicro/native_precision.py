"""Explicit, audited default-RoPE precision patch for the pinned CPU runtime."""
from pathlib import Path
import hashlib


def precise_default_rope(source: Path):
    path = source/'ggml/src/ggml-cpu/ops.cpp'
    original = path.read_text()
    edits = [
        ('static void ggml_rope_cache_init(\n     float theta_base, float freq_scale, const float * freq_factors, float corr_dims[2], int64_t ne0, float ext_factor, float mscale,\n     float * cache, float sin_sign, float theta_scale) {',
         'static void ggml_rope_cache_init(\n     float theta_base, float freq_scale, const float * freq_factors, float corr_dims[2], int64_t ne0, float ext_factor, float mscale,\n     float * cache, float sin_sign, float theta_scale, float freq_base, int n_dims) {'),
        ('        rope_yarn(\n            theta/ff, freq_scale, corr_dims, i0, ext_factor, mscale, &cache[i0 + 0], &cache[i0 + 1]\n',
         '        // JMicro: avoid position-dependent FP32 recurrence error for unscaled RoPE.\n'
         '        // Calculate the same independent frequencies as the trained model.\n'
         '        const float angle = !freq_factors && freq_scale == 1.0f && ext_factor == 0.0f\n'
         '            ? theta_base * (1.0f / powf(freq_base, (float) i0 / n_dims))\n'
         '            : theta / ff;\n'
         '        rope_yarn(\n            angle, freq_scale, corr_dims, i0, ext_factor, mscale, &cache[i0 + 0], &cache[i0 + 1]\n'),
        ('ggml_rope_cache_init(p, freq_scale, freq_factors, corr_dims, ne0, ext_factor, attn_factor, cache, sin_sign, theta_scale);',
         'ggml_rope_cache_init(p, freq_scale, freq_factors, corr_dims, ne0, ext_factor, attn_factor, cache, sin_sign, theta_scale, freq_base, n_dims);'),
    ]
    start = original.index('static void ggml_rope_cache_init(')
    end = original.index('static void ggml_mrope_cache_init(', start)
    block = original[start:end]
    for index, (before, after) in enumerate(edits[:2]):
        if block.count(before) != 1:
            raise ValueError(f'Pinned CPU RoPE source edit {index} has {block.count(before)} matches; refuse an unreviewed patch')
        block = block.replace(before, after)
    patched = original[:start]+block+original[end:]
    before, after = edits[2]
    if patched.count(before) != 1:
        raise ValueError('Pinned CPU RoPE call differs; refuse an unreviewed patch')
    patched = patched.replace(before, after)
    path.write_text(patched)
    return {'name': 'independent-default-rope-f32-v1', 'file': 'ggml/src/ggml-cpu/ops.cpp',
            'original_sha256': hashlib.sha256(original.encode()).hexdigest(),
            'patched_sha256': hashlib.sha256(patched.encode()).hexdigest(),
            'patcher_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope': 'CPU default unscaled RoPE only; scaling/YaRN/MRoPE retain upstream arithmetic'}
