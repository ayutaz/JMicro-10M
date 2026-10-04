"use strict";
const $ = id => document.getElementById(id);
let controller = null;
let generatedText = "";
let generationReady = false;
const stopLabels = {stop_id: "EOSで停止", max_new_tokens: "生成量の上限で停止", time_limit: "時間の上限で停止", server_stopping: "サーバーが停止"};

function updateControls() {
  $("max-value").textContent = `${$("max-new-tokens").value} tokens`;
  $("temperature-value").textContent = Number($("temperature").value).toFixed(2);
  $("top-p-value").textContent = Number($("top-p").value).toFixed(2);
  const greedy = $("mode").value === "greedy";
  $("temperature").disabled = greedy;
  $("top-p").disabled = greedy;
  $("seed").disabled = greedy;
}
function busy(active) {
  $("generate").disabled = active || !generationReady;
  $("stop").hidden = !active;
  $("output").setAttribute("aria-busy", String(active));
}
for (const id of ["max-new-tokens", "temperature", "top-p", "mode"]) $(id).addEventListener("input", updateControls);
$("prompt").addEventListener("input", () => { $("input-length").textContent = `${Array.from($("prompt").value).length} 文字`; });
document.querySelectorAll("[data-example]").forEach(button => button.addEventListener("click", () => {
  $("prompt").value = button.dataset.example;
  $("prompt").dispatchEvent(new Event("input"));
  $("prompt").focus();
}));
$("stop").addEventListener("click", () => controller?.abort());
$("copy").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(generatedText);
    $("copy").textContent = "コピーしました";
    setTimeout(() => { $("copy").textContent = "コピー"; }, 1500);
  } catch { $("error").hidden = false; $("error").textContent = "コピーできませんでした。生成文を選択してコピーしてください。"; }
});

function handleEvent(event) {
  if (event.type === "error") throw new Error(event.error);
  if (event.type === "start") $("status").textContent = `生成中 · 入力 ${event.input_tokens} tokens`;
  if (event.type === "token" || event.type === "done") {
    generatedText = event.text;
    $("output").textContent = generatedText;
    $("copy").disabled = !generatedText;
    $("metrics").textContent = `${event.generated_tokens} tokens`;
  }
  if (event.type === "done") {
    $("status").textContent = stopLabels[event.stop_reason] || event.stop_reason;
    $("metrics").textContent = `${event.generated_tokens} tokens · ${event.seconds.toFixed(2)} 秒 · ${event.tokens_per_second.toFixed(1)} tok/s`;
    if (event.truncated_utf8_tail) $("status").textContent += " · 末尾の未完成文字は保留";
    else if (!event.raw_valid_utf8) { $("error").hidden = false; $("error").textContent = "生成に不正な文字が含まれています。"; }
  }
}

$("form").addEventListener("submit", async event => {
  event.preventDefault();
  if (controller || !generationReady) return;
  controller = new AbortController();
  busy(true);
  generatedText = "";
  $("output").textContent = "";
  $("copy").disabled = true;
  $("error").hidden = true;
  $("status").textContent = "生成を準備中…";
  $("metrics").textContent = "—";
  try {
    const response = await fetch("/api/generate", {
      method: "POST", headers: {"Content-Type": "application/json"}, signal: controller.signal,
      body: JSON.stringify({prompt: $("prompt").value, mode: $("mode").value,
        max_new_tokens: Number($("max-new-tokens").value), temperature: Number($("temperature").value),
        top_p: Number($("top-p").value), seed: Number($("seed").value)})
    });
    if (!response.ok) throw new Error((await response.json()).error || "生成に失敗しました。");
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let pending = "", completed = false;
    for (;;) {
      const {value, done} = await reader.read();
      pending += decoder.decode(value, {stream: !done});
      const lines = pending.split("\n");
      pending = lines.pop();
      for (const line of lines) {
        if (!line.trim()) continue;
        const update = JSON.parse(line);
        handleEvent(update);
        if (update.type === "done") completed = true;
      }
      if (done) break;
    }
    if (!completed) throw new Error("生成途中で接続が切れました。再実行してください。");
  } catch (error) {
    if (error.name === "AbortError") $("status").textContent = "手動で停止";
    else { $("status").textContent = "生成できませんでした"; $("error").textContent = error.message; $("error").hidden = false; }
  } finally { controller = null; busy(false); }
});

async function loadModel() {
  busy(false);
  try {
    const response = await fetch("/api/model");
    if (!response.ok) throw new Error("サーバーに接続できません。");
    const model = await response.json();
    $("connection").textContent = "ローカル接続済み";
    $("connection").classList.add("ready");
    $("device").textContent = `WSL · ${model.device.replace("NVIDIA GeForce ", "")}`;
    $("training").textContent = `${(model.training_tokens / 1e9).toFixed(0)}B tokens 学習済み`;
    $("runtime").textContent = `${model.precision}\n文脈上限 ${model.context} tokens\n${model.parameters.toLocaleString()} parameters\ncheckpoint update ${model.update}\nSHA256 ${model.checkpoint_sha256.slice(0, 16)}…`;
    generationReady = true;
    busy(false);
  } catch (error) { $("connection").textContent = "接続できません"; $("error").hidden = false; $("error").textContent = error.message; }
}
updateControls();
loadModel();
