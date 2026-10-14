# Third-party notices

Akebono-10M-chat's own model, trained tokenizer and application are Apache-2.0. This does not replace the licenses of the following dependencies. Their distributed artifacts are copied without modification; worker.js contains a compiled bundle of ONNX Runtime Web and this application's inference code.

- ONNX Runtime Web 1.30.0: Copyright (c) Microsoft Corporation. MIT License, reproduced in LICENSE_ONNXRUNTIME.txt. Additional upstream notices are reproduced in ONNXRUNTIME_THIRD_PARTY_NOTICES.txt. Source: https://github.com/microsoft/onnxruntime/tree/v1.30.0
- @mlc-ai/web-tokenizers 0.1.6 / tokenizers-cpp: MLC-AI contributors, Apache License 2.0 (LICENSE). Source: https://github.com/mlc-ai/tokenizers-cpp . tokenizers.js is the unmodified npm artifact, including its embedded WASM.
- SentencePiece: Copyright 2016 Google Inc. Apache License 2.0 (LICENSE). Source: https://github.com/google/sentencepiece . Used through the existing tokenizers-cpp WASM binding, not through a reimplementation of its normalization.
- Hugging Face tokenizers: Hugging Face contributors, Apache License 2.0 (LICENSE). Source: https://github.com/huggingface/tokenizers . Included in the tokenizers-cpp distribution; this app selects its SentencePiece interface.
- TypeScript runtime helpers embedded in tokenizers.js: Copyright (c) Microsoft Corporation. MIT License (LICENSE_ONNXRUNTIME.txt contains the same Microsoft MIT license text). The original copyright and license comments remain in tokenizers.js.

The original model's training-source attribution is preserved in MODEL_CARD.md and the public model repository. Third-party libraries and original data sources do not endorse this model.
