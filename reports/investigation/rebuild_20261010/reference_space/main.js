const $ = id => document.getElementById(id);
const worker = new Worker(new URL('worker.js', import.meta.url));
let ready = false, busy = false, sequence = 0, current = null;
const reasons = { END: 'END', EOS: 'EOS', max_new_tokens: '生成トークン上限', context_limit: '文脈長上限', decoded_character_cap: '生成文字数上限' };
function controls() { $('input').disabled = !ready; $('send').disabled = !ready || busy; $('reset').disabled = !ready; }
function history(value) { $('history').textContent = `会話 ${value.completed_exchanges}往復 · 保存トークン ${value.stored_tokens} / ${value.context_limit}`; }
function message(speaker, body, metadata) {
  $('empty')?.remove();
  const node = document.createElement('article'); node.className = `message ${speaker}`;
  for (const [className, text] of [['speaker', speaker === 'user' ? 'あなた' : 'モデル'], ['body', body], ['metadata', metadata]]) {
    if (text === undefined) continue;
    const line = document.createElement('div'); line.className = className; line.textContent = text; node.append(line);
  }
  $('messages').append(node); $('messages').scrollTop = $('messages').scrollHeight;
}
$('input').addEventListener('input', () => { $('count').textContent = `${Array.from($('input').value).length} / 500文字`; });
$('input').addEventListener('keydown', event => {
  if (event.key === 'Enter' && !event.shiftKey && !event.isComposing) { event.preventDefault(); $('chat-form').requestSubmit(); }
});
$('chat-form').addEventListener('submit', event => {
  event.preventDefault(); if (!ready || busy) return;
  const text = $('input').value;
  if (!text.trim()) { $('status').textContent = '文章を入力してください。'; return; }
  if (Array.from(text).length > 500) { $('status').textContent = '入力は500文字以内にしてください。履歴は変更していません。'; return; }
  current = ++sequence; busy = true; controls(); $('status').textContent = 'CPUで生成中です。';
  worker.postMessage({ type: 'send', id: current, text });
});
$('reset').addEventListener('click', () => {
  current = ++sequence; busy = true; controls();
  $('messages').replaceChildren();
  const empty = document.createElement('p'); empty.id = 'empty'; empty.textContent = '文章を入力して会話を始められます。'; $('messages').append(empty);
  $('input').value = ''; $('count').textContent = '0 / 500文字'; $('status').textContent = '会話をリセット中です。';
  worker.postMessage({ type: 'reset', id: current });
});
worker.onmessage = event => {
  const data = event.data;
  if (data.id !== undefined && data.id !== current) return;
  if (data.type === 'loading') $('status').textContent = data.text;
  if (data.type === 'ready') { ready = true; $('model').textContent = data.model; history(data.history); $('status').textContent = '準備できました。'; controls(); }
  if (data.type === 'progress') $('status').textContent = `CPUで生成中です（${data.tokens}トークン）。`;
  if (data.type === 'answer') {
    message('user', data.user);
    const audit = data.generation_integrity.format_valid ? '形式検査 OK' : '形式の乱れあり';
    message('assistant', data.display_text, `終了: ${reasons[data.stop_reason] || data.stop_reason} · ${data.raw_generated_ids.length}トークン · ${audit}`);
    $('input').value = ''; $('count').textContent = '0 / 500文字';
    history(data.history); busy = false; $('status').textContent = `生成を終了しました（${reasons[data.stop_reason] || data.stop_reason}）。`; controls();
  }
  if (data.type === 'reset') { history(data.history); busy = false; $('status').textContent = '会話をリセットしました。'; controls(); }
  if (data.type === 'error') { history(data.history); busy = false; $('status').textContent = data.text; controls(); }
  if (data.type === 'fatal') { ready = false; busy = false; $('status').textContent = `起動できませんでした: ${data.text}`; controls(); }
};
worker.onerror = () => { ready = false; busy = false; $('status').textContent = 'ブラウザーでの実行に失敗しました。ページを再読み込みしてください。'; controls(); };
