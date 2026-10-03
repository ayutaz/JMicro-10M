"""Explicit, audited default-RoPE precision patch for the pinned CPU runtime."""
from pathlib import Path
import hashlib


def validate_stable_runtime(runtime: Path):
    """Bind the patched CPU source and the executable/shared libraries in use."""
    import json
    receipt = json.loads((runtime/'source_receipt.json').read_text())
    assert receipt['revision'] == '46ca246de9bb1c35269722a6240d37d9dfd79cad'
    assert receipt['archive_sha256'] == 'ce86fc42c03c5b93d25cd8b555bce6660b684f131e2047d4265bbb07fa1e9ceb'
    assert any(patch['name']=='stable-f32-accumulation-v2' for patch in receipt['patches']), 'Stable FP32 runtime is required'
    for patch in receipt['patches']:
        entries = patch.get('files',[patch])
        for entry in entries:
            expected = entry.get('final_patched_sha256',entry['patched_sha256'])
            assert hashlib.sha256((runtime/'llama.cpp'/entry['file']).read_bytes()).hexdigest() == expected
    assert hashlib.sha256((runtime/'llama-bridge').read_bytes()).hexdigest() == receipt['bridge_binary_sha256']
    assert receipt['shared_library_sha256'], 'Native shared library bindings are required'
    for name, digest in receipt['shared_library_sha256'].items():
        assert hashlib.sha256((runtime/name).read_bytes()).hexdigest() == digest
    assert any('-DGGML_LLAMAFILE=OFF' in command for command in receipt['commands'])
    assert any('-DCMAKE_CXX_FLAGS=-ffp-contract=off' in command for command in receipt['commands'])
    return receipt


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


def stable_f32_accumulation(source: Path):
    """Separate CPU reference runtime: F32 storage, F64 products/reductions.

    This changes real native inference, rather than comparing native logits to
    themselves or changing the verifier's tolerance. Quantized kernels retain
    their upstream implementations. Disable llamafile in the matching build so
    it cannot bypass the F32 dot-product kernel.
    """
    receipts = []
    path = source/'ggml/src/ggml-cpu/vec.cpp'
    original = path.read_text()
    patched = original
    replacements = {
        'void ggml_vec_dot_f32(': '''void ggml_vec_dot_f32(int n, float * GGML_RESTRICT s, size_t bs, const float * GGML_RESTRICT x, size_t bx, const float * GGML_RESTRICT y, size_t by, int nrc) {
    assert(nrc == 1);
    GGML_UNUSED(bs); GGML_UNUSED(bx); GGML_UNUSED(by); GGML_UNUSED(nrc);
    double sum = 0.0;
    for (int i = 0; i < n; ++i) sum += (double)x[i] * (double)y[i];
    *s = (float)sum;
}''',
        'void ggml_vec_silu_f32(': '''void ggml_vec_silu_f32(const int n, float * y, const float * x) {
    for (int i = 0; i < n; ++i) y[i] = (float)((double)x[i] / (1.0 + exp(-(double)x[i])));
}''',
        'ggml_float ggml_vec_soft_max_f32(': '''ggml_float ggml_vec_soft_max_f32(const int n, float * y, const float * x, float max) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        const float shifted = x[i] - max;
        const float value = (float)exp((double)shifted);
        y[i] = value;
        sum += (double)value;
    }
    return sum;
}''',
    }
    for signature, replacement in replacements.items():
        if patched.count(signature) != 1:
            raise ValueError(f'Pinned precision function differs: {signature}')
        start = patched.index(signature)
        opening = patched.index('{', start)
        depth, end = 1, opening + 1
        while depth:
            depth += (patched[end] == '{') - (patched[end] == '}')
            end += 1
        patched = patched[:start] + replacement + patched[end:]
    path.write_text(patched)
    receipts.append({'file':str(path.relative_to(source)),
                     'original_sha256':hashlib.sha256(original.encode()).hexdigest(),
                     'patched_sha256':hashlib.sha256(patched.encode()).hexdigest()})
    path = source/'ggml/src/ggml-cpu/ops.cpp'
    original = path.read_text()
    start = original.index('static void ggml_compute_forward_rms_norm_f32(')
    end = original.index('\nvoid ggml_compute_forward_rms_norm(', start)
    block = original[start:end]
    before = 'sum += (ggml_float)(x[i00] * x[i00]);'
    if block.count(before) != 1:
        raise ValueError('Pinned RMSNorm reduction differs')
    block = block.replace(before, 'sum += (double)x[i00] * (double)x[i00];')
    patched = original[:start]+block+original[end:]
    start = patched.index('static void ggml_rope_cache_init(')
    end = patched.index('static void ggml_mrope_cache_init(', start)
    block = patched[start:end]
    before = '''        rope_yarn(
            angle, freq_scale, corr_dims, i0, ext_factor, mscale, &cache[i0 + 0], &cache[i0 + 1]
        );'''
    after = '''        if (!freq_factors && freq_scale == 1.0f && ext_factor == 0.0f) {
            // Round double transcendental results at the same F32 boundary.
            cache[i0 + 0] = (float)cos((double)angle) * mscale;
            cache[i0 + 1] = (float)sin((double)angle) * mscale;
        } else {
            rope_yarn(angle, freq_scale, corr_dims, i0, ext_factor, mscale,
                      &cache[i0 + 0], &cache[i0 + 1]);
        }'''
    if block.count(before) != 1:
        raise ValueError('Pinned independent default RoPE trig source differs')
    block = block.replace(before, after)
    patched = patched[:start]+block+patched[end:]
    path.write_text(patched)
    receipts.append({'file':str(path.relative_to(source)),
                     'original_sha256':hashlib.sha256(original.encode()).hexdigest(),
                     'patched_sha256':hashlib.sha256(patched.encode()).hexdigest()})
    return {'name':'stable-f32-accumulation-v2', 'files':receipts,
            'patcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'CPU F32 dot, RMSNorm, SiLU, softmax and unscaled RoPE trig; F32 storage/output, F64 accumulation; llamafile disabled'}
