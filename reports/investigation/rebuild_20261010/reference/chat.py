"""Self-contained CPU FP32 inference for the experimental v19 weights."""
import os
import sys
from pathlib import Path

os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ['HIP_VISIBLE_DEVICES'] = ''
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import argparse
import hashlib
import json
import time
import torch
from safetensors.torch import load_file
from modeling_japanesechat10m import Config, JapaneseLM
from tokenizer import Tokenizer
from output_integrity import escape_controls, generation_integrity

HERE = Path(__file__).resolve().parent
CONTEXT = 512
RESERVE = 16
MAX_NEW = 128
CHAR_CAP = 160


def digest(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


class ContextFull(ValueError):
    pass


class Chat:
    def __init__(self, model_dir=None, threads=2):
        torch.set_num_threads(threads)
        self.directory = Path(model_dir).resolve() if model_dir else HERE
        self.meta = json.loads((self.directory / 'runtime.json').read_text('utf-8'))
        config = json.loads((self.directory / 'config.json').read_text('utf-8'))
        self.frame = self.meta['system_frame']
        self.notice = '実験的10M日本語モデルです。誤答や履歴の取り違えがあります。'
        self.checkpoint_path = self.directory / self.meta['weights']
        token_path = self.directory / self.meta['tokenizer']
        if digest(self.checkpoint_path) != self.meta['weights_sha256']:
            raise ValueError('Weights SHA256 mismatch.')
        if digest(token_path) != self.meta['tokenizer_sha256']:
            raise ValueError('Tokenizer SHA256 mismatch.')
        expected_generation = dict(decoder='greedy_argmax', max_new_tokens=MAX_NEW,
                                   decoded_character_cap=CHAR_CAP, context_limit=CONTEXT,
                                   minimum_answer_reserve_tokens=RESERVE)
        if self.meta['generation'] != expected_generation:
            raise ValueError('Runtime generation settings mismatch.')
        self.model = JapaneseLM(Config(**config)).cpu().float()
        self.model.load_state_dict(load_file(str(self.checkpoint_path), device='cpu'), strict=True)
        self.model.eval()
        self.parameters = sum(p.numel() for p in self.model.parameters())
        assert self.parameters == 9965824
        assert all(p.device.type == 'cpu' and p.dtype == torch.float32 for p in self.model.parameters())
        assert not torch.cuda.is_initialized(), 'CPU runtime must not initialize a GPU.'
        self.tok = Tokenizer(token_path)
        assert self.tok.sp.vocab_size() == 12288
        assert (self.tok.pad, self.tok.unk, self.tok.bos, self.tok.eos,
                self.tok.system, self.tok.user, self.tok.assistant,
                self.tok.end, self.tok.newline) == tuple(range(9))
        self.reset()

    def reset(self):
        self.users = []
        self.bodies = []

    def status(self):
        base = [self.tok.bos, self.tok.system] + self.tok.encode(self.frame) + [self.tok.end]
        stored = len(base) + sum(4 + len(self.tok.encode(u)) + len(b)
                                 for u, b in zip(self.users, self.bodies))
        return dict(model=self.meta['identifier'], completed_exchanges=len(self.users),
                    stored_tokens=stored, context_limit=CONTEXT, device='cpu',
                    precision='FP32', GPU_initialized=torch.cuda.is_initialized(),
                    dropped_history_turns=0)

    def prefix(self, user):
        ids = [self.tok.bos, self.tok.system] + self.tok.encode(self.frame) + [self.tok.end]
        for i, u in enumerate(self.users + [user]):
            ids += [self.tok.user] + self.tok.encode(u) + [self.tok.end, self.tok.assistant]
            if i < len(self.bodies):
                ids += list(self.bodies[i]) + [self.tok.end]
        return ids

    @torch.inference_mode()
    def send(self, user):
        if not user.strip():
            raise ValueError('空の入力は送信しません。')
        prefix = self.prefix(user)
        if len(prefix) > CONTEXT - RESERVE:
            raise ContextFull(f'入力と履歴が {len(prefix)} トークンです。'
                              f'上限512（回答用に16確保）を超えるため送信しません。'
                              '入力を短くするか /reset で新しい会話を始めてください。履歴は削除していません。')
        started = time.perf_counter()
        raw, body = [], []
        reason = 'max_new_tokens'
        for _ in range(MAX_NEW):
            if len(prefix) + len(raw) > CONTEXT:
                reason = 'context_limit'
                break
            logits, _ = self.model(torch.tensor([prefix + raw], dtype=torch.long, device='cpu'))
            last = logits[0, -1].float()
            if not torch.isfinite(last).all().item():
                raise RuntimeError('Non-finite model output; this turn was not added to history.')
            token = int(last.argmax())
            raw.append(token)
            if token in (self.tok.end, self.tok.eos):
                reason = 'END' if token == self.tok.end else 'EOS'
                break
            body.append(token)
            if len(self.tok.decode(body)) >= CHAR_CAP:
                reason = 'decoded_character_cap'
                break
        text = self.tok.decode(body, visible_controls=True)
        audit = generation_integrity(body, self.tok)
        self.users.append(user)
        # Keep actual generated IDs, including visible malformed controls. Never re-encode replies.
        self.bodies.append(list(body))
        return dict(user=user, text=text, body_ids=body, raw_generated_ids=raw,
                    input_ids=prefix, input_tokens=len(prefix), body_tokens=len(body),
                    seconds=time.perf_counter() - started, stop_reason=reason,
                    generation_integrity=audit, history=self.status())


def main():
    parser = argparse.ArgumentParser(description='JapaneseChat10M CPU local chat; no server or external calls.')
    parser.add_argument('--model-dir', type=Path, default=HERE, help='Local directory containing the packaged files.')
    parser.add_argument('--threads', type=int, choices=range(1, 9), default=2)
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='backslashreplace')
    started = time.perf_counter()
    print('CPUモデルを読み込み中…', flush=True)
    chat = Chat(args.model_dir, args.threads)
    print(f'JapaneseChat10M / {chat.meta["model_name"]} / {chat.parameters:,} parameters / CPU FP32', flush=True)
    print(f'読み込み {time.perf_counter() - started:.2f}秒。実験的10M日本語モデルです。', flush=True)
    print(f'weights: {chat.checkpoint_path.name}', flush=True)
    print(f'SHA256: {chat.meta["weights_sha256"]}', flush=True)
    print(chat.notice, flush=True)
    print('日本語を入力してEnter。/reset 履歴初期化、/status 使用量、/help 説明、/quit 終了。', flush=True)
    print('履歴は自動で削りません。回答は最大128トークン・160文字目安、途中停止も表示します。', flush=True)
    while True:
        try:
            user = input('あなた: ')
        except (EOFError, KeyboardInterrupt):
            print('\n終了しました。', flush=True)
            break
        if user in ('/quit', '/exit'):
            print('終了しました。', flush=True)
            break
        if user == '/reset':
            chat.reset()
            print('履歴を初期化しました。新しい会話です。', flush=True)
            continue
        if user == '/status':
            state = chat.status()
            print(f'モデル={state["model"]}、{state["completed_exchanges"]}往復、'
                  f'保存済み履歴={state["stored_tokens"]}/512トークン、CPU、履歴削除0。', flush=True)
            continue
        if user == '/help':
            print('送信: 日本語を1行入力しEnter。履歴はこの窓のメモリだけに保持します。\n'
                  '/reset は全履歴を消します。終了・再起動でも履歴は消えます。\n'
                  '512トークンには役割・システム文・入力・回答が含まれます。上限付近では送信を拒否します。\n'
                  'END/EOSは回答終端です。それ以外の停止は途中の回答で、表示した部分も履歴に残ります。\n'
                  '返答はモデルの生成そのままで、反復・誤答・空の返答も表示します。\n'
                  'v19の独自CPU推論コードです。誤答や履歴の取り違えがあります。', flush=True)
            continue
        try:
            result = chat.send(user)
        except (ContextFull, ValueError) as error:
            print(str(error), flush=True)
            continue
        except KeyboardInterrupt:
            print('\n生成を中断しました。この入力と途中の回答は履歴に追加していません。', flush=True)
            continue
        print('モデル: ' + (escape_controls(result['text']) if result['text'] else '[空の返答]'), flush=True)
        print(f'[{result["seconds"]:.2f}秒 / 停止={result["stop_reason"]} / '
              f'入力{result["input_tokens"]}・回答{result["body_tokens"]}トークン]', flush=True)
        if result['stop_reason'] not in ('END', 'EOS'):
            print('回答は途中で停止しました。表示した部分を履歴に残しています。', flush=True)
        if not result['generation_integrity']['format_valid']:
            print('生成形式エラー: ' + json.dumps(result['generation_integrity'], ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
