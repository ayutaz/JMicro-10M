import sentencepiece as spm
SYMBOLS=['<|system|>','<|user|>','<|assistant|>','<|end|>','<|newline|>']
class Tokenizer:

    def __init__(self, path):
        self.sp = spm.SentencePieceProcessor(model_file=str(path))
        self.pad, self.unk, self.bos, self.eos = (0, 1, 2, 3)
        self.system, self.user, self.assistant, self.end, self.newline = [self.sp.piece_to_id(s) for s in SYMBOLS]
        self.byte_ids = {i for i in range(self.sp.vocab_size()) if self.sp.is_byte(i)}
        assert all((i >= 4 for i in [self.system, self.user, self.assistant, self.end, self.newline]))

    def encode(self, text):
        lines = text.split('\n')
        out = []
        for j, line in enumerate(lines):
            if j:
                out.append(self.newline)
            out.extend(self.sp.encode(line, out_type=int))
        return out

    def decode(self, ids, visible_controls=True):
        parts = []
        chunk = []
        controls = {self.pad, self.unk, self.bos, self.eos, self.system, self.user, self.assistant, self.end}
        for i in ids:
            if i == self.newline:
                parts.append(self.sp.decode(chunk))
                chunk = []
                parts.append('\n')
            elif i in controls:
                if visible_controls:
                    parts.append(self.sp.decode(chunk))
                    chunk = []
                    parts.append(self.sp.id_to_piece(i))
            else:
                chunk.append(i)
        parts.append(self.sp.decode(chunk))
        return ''.join(parts)
