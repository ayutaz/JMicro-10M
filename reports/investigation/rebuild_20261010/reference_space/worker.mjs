import { ChatEngine, escapeControls } from './engine.mjs';

let engine, revision = 0, chain = Promise.resolve();
const emit = (type, values = {}) => postMessage({ type, ...values });
const root = new URL('./', self.location.href).href;
async function download(file) {
  const response = await fetch(new URL(file, root), { credentials: 'omit' });
  if (!response.ok) throw new Error(`${file}を取得できませんでした (${response.status})。`);
  return response.arrayBuffer();
}
async function hash(bytes) {
  return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)), b => b.toString(16).padStart(2, '0')).join('');
}
async function boot() {
  emit('loading', { text: 'モデルを読み込み中です（初回は約60 MB）。' });
  importScripts(new URL('tokenizers.js', root).href);
  const runtime = JSON.parse(new TextDecoder().decode(await download('runtime.json')));
  const [model, tokenizer] = await Promise.all([download(runtime.onnx_file), download(runtime.tokenizer_file)]);
  if (model.byteLength !== runtime.onnx_bytes || await hash(model) !== runtime.onnx_sha256 || await hash(tokenizer) !== runtime.tokenizer_sha256) {
    throw new Error('モデルまたはtokenizerの検証に失敗しました。');
  }
  emit('loading', { text: 'ブラウザーのCPU推論を準備中です。' });
  engine = await ChatEngine.create(new Uint8Array(model), tokenizer, runtime, root);
  emit('ready', { history: engine.status(), model: runtime.identifier });
}
const ready = boot();
ready.catch(error => emit('fatal', { text: error.message }));
self.onmessage = event => {
  const request = event.data;
  if (request.type === 'reset') revision++;
  const thisRevision = revision;
  chain = chain.catch(() => {}).then(async () => {
    await ready;
    if (request.type === 'reset') {
      engine.reset();
      emit('reset', { id: request.id, history: engine.status() });
    } else if (request.type === 'send') {
      if (thisRevision !== revision) return;
      try {
        const answer = await engine.send(request.text,
          progress => emit('progress', { id: request.id, ...progress }),
          () => thisRevision !== revision);
        if (thisRevision === revision) emit('answer', { id: request.id, ...answer, display_text: escapeControls(answer.text) });
      } catch (error) {
        if (thisRevision === revision) emit('error', { id: request.id, text: error.message, history: engine.status() });
      }
    }
  }).catch(error => emit('fatal', { text: error.message }));
};
