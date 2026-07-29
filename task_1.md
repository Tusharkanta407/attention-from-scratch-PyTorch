# 📅 Attention From Scratch - Learning Checklist

## **Day 1: Setup & Configuration (1 Hour)**
- [ ] Initialize Python Virtual Environment (`.venv`) and check package installations.
- [ ] Implement `src/lotr_transformer/config.py` (defining model and data hyperparameters using python dataclasses).
- [ ] Create `configs/default.yaml` (specifying default training and model hyperparameters).
- [ ] Implement `src/lotr_transformer/vocab.py` (vocabulary building, token-to-idx mapping, min frequency filtering, and `<UNK>` token fallback).
- [ ] Implement dataset downloader script `scripts/download_data.py`.

## **Day 2: Data Pipeline & Embeddings (2 Hours)**
- [ ] Implement tokenization utilities and custom spacy/unicode tokenizer in `src/lotr_transformer/data.py`.
- [ ] Build `LOTRDataset` (yielding input-target shifted pairs) in `src/lotr_transformer/data.py`.
- [ ] Implement `ScaledEmbedding` in `src/lotr_transformer/embeddings.py`.
- [ ] Implement `PositionalEncoding` (sin/cos sinusoidal functions) in `src/lotr_transformer/embeddings.py`.

## **Day 3: Attention & Architecture (2 Hours)**
- [ ] Implement scaled dot-product `attention` function and look-ahead causal mask in `src/lotr_transformer/attention.py`.
- [ ] Build `MultiHeadedAttention` layer in `src/lotr_transformer/layers.py`.
- [ ] Build `DecoderLayer` block in `src/lotr_transformer/layers.py`.
- [ ] Assemble full `TransformerDecoder` network in `src/lotr_transformer/model.py`.

## **Day 4: Training, Generation & CLI (2 Hours)**
- [ ] Implement model checkpoint saving/loading utilities in `src/lotr_transformer/utils.py`.
- [ ] Implement the label-smoothed cross-entropy loss training loop in `src/lotr_transformer/train_loop.py`.
- [ ] Implement autoregressive text generation and evaluation in `src/lotr_transformer/generate.py`.
- [ ] Create loss plotting utility in `src/lotr_transformer/visualize.py`.
- [ ] Set up the CLI commands in `scripts/run.py`.
- [ ] Run end-to-end training and generate sample text!
