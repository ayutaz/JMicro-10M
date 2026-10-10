"""Complete dialogue targets with resumable Assistant-body/EOT supervision.

The sampler returns already shifted targets for Trainer.step; it never packs
unrelated dialogues together or truncates a current user/assistant pair.
"""
import hashlib
import json

import numpy as np
import torch


class AssistantSampler:
    def __init__(self, records, tokenizer, context, seed):
        if context < 2 or not records:
            raise ValueError("Nonempty train dialogues and context >= 2 required")
        self.context, self.seed = context, seed
        self.windows = []
        families = set()
        for record in records:
            if record.get("split") != "train":
                raise ValueError("Only train dialogues may be sampled")
            family = record["doc_id"]
            if family in families:
                raise ValueError("Duplicate dialogue identity")
            families.add(family)
            messages = record.get("messages")
            if messages is None:
                messages = json.loads(record["messages_json"])
            roles = [message["role"] for message in messages]
            offset = int(bool(roles) and roles[0] == "system")
            if (not roles[offset:] or roles[offset:] != [
                    "user" if i % 2 == 0 else "assistant"
                    for i in range(len(roles) - offset)]):
                raise ValueError("Dialogue must alternate user/assistant after optional system")
            before = len(self.windows)
            # context counts model inputs; the final EOT is a target, not input.
            for window in tokenizer.sft_windows(messages, context=context + 1):
                ids = np.asarray(window["input_ids"], dtype=np.int64)
                labels = np.asarray(window["labels"], dtype=np.int64)
                if len(ids) > context + 1 or len(ids) != len(labels):
                    raise ValueError("Complete assistant target exceeds context")
                selected = labels[labels != -100]
                if (not len(selected) or selected[-1] != 7 or
                        np.any((selected[:-1] < 8)) or len(selected) != window["target_tokens"]):
                    raise ValueError("Labels must contain one Assistant body followed by EOT")
                self.windows.append(dict(ids=ids, labels=labels, doc_id=family,
                    target_message_index=window["target_message_index"],
                    removed_turns=window["removed_turns"]))
            if len(self.windows) == before:
                raise ValueError("Every dialogue must contain an assistant target")
        digest = hashlib.sha256()
        for window in self.windows:
            digest.update(json.dumps([window["doc_id"], window["target_message_index"]], ensure_ascii=False).encode())
            digest.update(window["ids"].astype("<i8").tobytes())
            digest.update(window["labels"].astype("<i8").tobytes())
        self.binding = digest.hexdigest()
        self.byte_lengths = np.asarray([0 if i < 8 else len(tokenizer.decode_bytes([i])) for i in range(tokenizer.vocab_size)])
        self.epoch = self.position = 0
        self.series_tokens = self.input_tokens = self.teacher_tokens = 0
        self.physical_tokens = self.eot_teachers = self.examples = self.removed_turns = 0
        self._shuffle()

    def _shuffle(self):
        self.order = np.random.default_rng(np.random.SeedSequence([self.seed, self.epoch])).permutation(len(self.windows))

    def state_dict(self):
        return dict(kind="assistant-complete-window-v1", binding=self.binding,
            context=self.context, seed=self.seed, windows=len(self.windows),
            epoch=self.epoch, position=self.position, series_tokens=self.series_tokens,
            input_tokens=self.input_tokens, teacher_tokens=self.teacher_tokens,
            physical_tokens=self.physical_tokens, eot_teachers=self.eot_teachers,
            examples=self.examples, removed_turns=self.removed_turns)

    def load_state_dict(self, state):
        current = self.state_dict()
        if any(state[k] != current[k] for k in ("kind", "binding", "context", "seed", "windows")):
            raise ValueError("Dialogue data, masks or sampler configuration differ")
        keys = ("epoch", "position", "series_tokens", "input_tokens", "teacher_tokens",
                "physical_tokens", "eot_teachers", "examples", "removed_turns")
        if any(type(state[k]) is not int or state[k] < 0 for k in keys):
            raise ValueError("Invalid dialogue counters")
        if not 0 <= state["position"] <= len(self.windows):
            raise ValueError("Invalid dialogue cursor")
        if (state["examples"] != state["epoch"] * len(self.windows) + state["position"] or
                state["eot_teachers"] != state["examples"] or
                state["series_tokens"] != state["input_tokens"] + state["examples"] or
                not state["eot_teachers"] <= state["teacher_tokens"] <= state["input_tokens"] <= state["physical_tokens"]):
            raise ValueError("Inconsistent dialogue accounting")
        for key in keys:
            setattr(self, key, state[key])
        self._shuffle()

    def batch(self, size):
        if type(size) is not int or size <= 0:
            raise ValueError("Positive batch size required")
        x = np.zeros((size, self.context), dtype=np.int64)
        y = np.full((size, self.context), -100, dtype=np.int64)
        body_bytes = 0
        for row in range(size):
            if self.position == len(self.windows):
                self.epoch += 1
                self.position = 0
                self._shuffle()
            window = self.windows[int(self.order[self.position])]
            ids, labels = window["ids"], window["labels"]
            count = len(ids) - 1
            x[row, :count], y[row, :count] = ids[:-1], labels[1:]
            teachers = labels[labels != -100]
            body_bytes += int(self.byte_lengths[teachers].sum())
            self.series_tokens += len(ids)
            self.input_tokens += count
            self.teacher_tokens += len(teachers)
            self.eot_teachers += 1
            self.examples += 1
            self.removed_turns += window["removed_turns"]
            self.position += 1
        self.physical_tokens += size * self.context
        return torch.from_numpy(x), torch.from_numpy(y), body_bytes
