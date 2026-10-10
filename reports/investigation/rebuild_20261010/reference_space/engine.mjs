import * as ort from 'onnxruntime-web/wasm';

const CONTROL_IDS = new Set([0, 1, 2, 3, 4, 5, 6, 7]);
const UNEXPECTED_IDS = new Set([0, 1, 2, 4, 5, 6]);
const nonprinting = ch => /[\p{Cc}\p{Cs}]/u.test(ch) && !'\n\r\t'.includes(ch);
const codepoint = ch => ch.codePointAt(0).toString(16).toUpperCase().padStart(4, '0');

export function escapeControls(text) {
  return Array.from(text, ch => nonprinting(ch) ? '\\u' + ch.codePointAt(0).toString(16).padStart(4, '0') : ch).join('');
}

export class ChatEngine {
  constructor(tokenizer, session, runtime) {
    this.tokenizer = tokenizer;
    this.session = session;
    this.runtime = runtime;
    this.reset();
  }

  static async create(modelBytes, tokenizerBytes, runtime, wasmPaths) {
    const Tokenizer = globalThis.tokenizers?.Tokenizer;
    if (!Tokenizer) throw new Error('SentencePiece WASMを読み込めませんでした。');
    ort.env.wasm.numThreads = 1;
    ort.env.wasm.proxy = false;
    ort.env.logLevel = 'error';
    if (wasmPaths) ort.env.wasm.wasmPaths = wasmPaths;
    const tokenizer = await Tokenizer.fromSentencePiece(tokenizerBytes);
    if (tokenizer.getVocabSize() !== 12288) throw new Error('tokenizerの語彙数が一致しません。');
    const expected = ['<pad>', '<unk>', '<s>', '</s>', '<|system|>', '<|user|>', '<|assistant|>', '<|end|>', '<|newline|>'];
    for (let i = 0; i < expected.length; i++) {
      if (tokenizer.idToToken(i) !== expected[i]) throw new Error('特殊tokenの識別が一致しません。');
    }
    const session = await ort.InferenceSession.create(modelBytes, {
      executionProviders: ['wasm'], graphOptimizationLevel: 'all', logSeverityLevel: 3,
    });
    return new ChatEngine(tokenizer, session, runtime);
  }

  encode(text) {
    const ids = [];
    text.split('\n').forEach((line, i) => {
      if (i) ids.push(8);
      ids.push(...this.tokenizer.encode(line));
    });
    return ids;
  }

  decode(ids, visibleControls = true) {
    const parts = [];
    let chunk = [];
    const flush = () => { parts.push(this.tokenizer.decode(Int32Array.from(chunk))); chunk = []; };
    for (const id of ids) {
      if (id === 8) { flush(); parts.push('\n'); }
      else if (CONTROL_IDS.has(id)) {
        if (visibleControls) { flush(); parts.push(this.tokenizer.idToToken(id)); }
      } else chunk.push(id);
    }
    flush();
    return parts.join('');
  }

  reset() { this.users = []; this.bodies = []; }

  prefix(user) {
    const ids = [2, 4, ...this.encode(this.runtime.system_frame), 7];
    [...this.users, user].forEach((text, i) => {
      ids.push(5, ...this.encode(text), 7, 6);
      if (i < this.bodies.length) ids.push(...this.bodies[i], 7);
    });
    return ids;
  }

  status() {
    let stored = 3 + this.encode(this.runtime.system_frame).length;
    this.users.forEach((user, i) => { stored += 4 + this.encode(user).length + this.bodies[i].length; });
    return { completed_exchanges: this.users.length, stored_tokens: stored, context_limit: 512 };
  }

  audit(ids) {
    const text = this.decode(ids);
    const unexpected = [];
    ids.forEach((id, position) => {
      if (UNEXPECTED_IDS.has(id)) unexpected.push({ position, id, piece: this.tokenizer.idToToken(id) });
    });
    const controls = [];
    Array.from(text).forEach((ch, position) => {
      if (nonprinting(ch)) controls.push({ position, codepoint: 'U+' + codepoint(ch), category: /\p{Cs}/u.test(ch) ? 'Cs' : 'Cc' });
    });
    const replacements = Array.from(text).filter(ch => ch === '�').length;
    return {
      format_valid: !unexpected.length && !controls.length && !replacements,
      unexpected_controls: unexpected, decoded_nonprinting_controls: controls,
      decoded_replacement_characters: replacements, format_audit_version: 2,
      decode_preserves_control_tokens: true,
    };
  }

  async logits(ids) {
    if (ids.length < 1 || ids.length > 512) throw new Error('モデルへの入力長が上限を超えています。');
    const input = new ort.Tensor('int64', BigInt64Array.from(ids, BigInt), [1, ids.length]);
    let outputs;
    try {
      outputs = await this.session.run({ input_ids: input });
      const values = Float32Array.from(outputs.logits.data);
      if (values.length !== 12288 || !values.every(Number.isFinite)) throw new Error('モデルの出力が正常な数値ではありません。');
      return values;
    } finally {
      input.dispose();
      if (outputs) for (const tensor of Object.values(outputs)) tensor.dispose();
    }
  }

  async send(user, progress = () => {}, cancelled = () => false) {
    if (typeof user !== 'string' || !user.trim()) throw new Error('文章を入力してください。');
    if (Array.from(user).length > 500) throw new Error('入力は500文字以内にしてください。履歴は変更していません。');
    const prefix = this.prefix(user);
    if (prefix.length > 496) throw new Error(`入力と履歴が${prefix.length}トークンです。上限512（回答用に16確保）を超えるため送信しません。履歴は変更していません。`);
    const raw = [], body = [];
    let reason = 'max_new_tokens';
    for (let n = 0; n < 128; n++) {
      if (cancelled()) throw new Error('生成を中断しました。履歴は変更していません。');
      if (prefix.length + raw.length > 512) { reason = 'context_limit'; break; }
      const values = await this.logits([...prefix, ...raw]);
      let token = 0;
      for (let i = 1; i < values.length; i++) if (values[i] > values[token]) token = i;
      raw.push(token);
      if (token === 7 || token === 3) { reason = token === 7 ? 'END' : 'EOS'; break; }
      body.push(token);
      progress({ tokens: body.length });
      await new Promise(resolve => setTimeout(resolve, 0));
      if (Array.from(this.decode(body)).length >= 160) { reason = 'decoded_character_cap'; break; }
    }
    if (cancelled()) throw new Error('生成を中断しました。履歴は変更していません。');
    const text = this.decode(body);
    const audit = this.audit(body);
    this.users.push(user);
    this.bodies.push([...body]);
    return { user, text, body_ids: body, raw_generated_ids: raw, input_ids: prefix,
      stop_reason: reason, generation_integrity: audit, history: this.status() };
  }

  async dispose() { this.reset(); this.tokenizer.dispose(); await this.session.release(); }
}
