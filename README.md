#  Attention From Scratch: PyTorch Decoder-Only Transformer

<div align="center">
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License" />
</div>

<p align="center">
  <strong>A clean, from-scratch PyTorch implementation of a decoder-only Transformer</strong><br />
  <em>Inspired by "Attention Is All You Need" and trained on the Lord of the Rings corpus.</em>
</p>

---

##  About the Project

This repository contains my personal, step-by-step implementation of a decoder-only Transformer model. Written entirely from scratch for deep educational understanding, it features:
- **Decoder-Only Architecture**: Multi-head self-attention with causal masking for autoregressive next-token prediction.
- **spaCy Tokenization**: Robust NLP-based tokenization with a blank pipeline fallback.
- **Dynamic Vocabulary**: Built-in support for Out-Of-Vocabulary (OOV) tokens via `<UNK>` and minimum frequency filtering.
- **Reproducible Training**: Multi-stage setup supporting deterministic seeds, label-smoothed cross-entropy loss, and CLI tools.
- **Dockerized Environments**: Skeletons for both CPU and GPU containerized execution.

---

##  Project Structure

Here is the structured layout of the codebase we are building:

```text
attention-from-scratch-pytorch/
├── configs/
│   └── default.yaml         # Hyperparameter configurations (d_model, batch size, etc.)
├── docker/
│   ├── Dockerfile.cpu       # Container setup for CPU running
│   └── Dockerfile.gpu       # Container setup for GPU acceleration
├── scripts/
│   ├── download_data.py     # Script to download and unpack the LOTR raw text data
│   └── run.py               # CLI entrypoint to train or sample/evaluate checkpoints
├── src/
│   └── lotr_transformer/    # Main package containing custom modules
│       ├── __init__.py
│       ├── attention.py     # Scaled Dot-Product Attention & causal masking
│       ├── config.py        # Typed dataclasses for configuration loading
│       ├── data.py          # Tokenizer wrapper and PyTorch Dataset
│       ├── embeddings.py    # Embedding scaling and Sinusoidal Positional Encodings
│       ├── generate.py      # Autoregressive generation & sampling
│       ├── layers.py        # Multi-Head Attention & Decoder block modules
│       ├── model.py         # Complete TransformerDecoder assembly
│       ├── train_loop.py    # Training execution with label smoothing
│       ├── utils.py         # Checkpointing, seeding, and device helpers
│       └── vocab.py         # Token-to-ID vocabulary dictionary
└── tests/                   # Suite of unit tests for module verification
```

---

##  Quickstart (Local Development)

### 1. Environment Setup
Create a virtual environment, activate it, and install the required dependencies:

```bash
# Create and activate environment
python -m venv .venv
# On Windows (Git Bash):
source .venv/Scripts/activate
# On macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Fetch Training Data
Download the raw Lord of the Rings text corpus:
```bash
python -m scripts.download_data --out_dir data/raw
```

### 3. Run Training
Start training the Transformer decoder:
```bash
python -m scripts.run train --config configs/default.yaml
```

### 4. Text Generation (Sampling)
Once training is complete and you have saved a checkpoint, test the model by generating text:
```bash
python -m scripts.run sample --ckpt outputs/last.ckpt --start_tokens "The Where fight Gandalf" --num_tokens 128
```

---

##  Unit Testing & Verification

Run the test suite to verify the custom model logic (attention matrices, dataset offset mappings, and positional encoding):

```bash
# Add src to PYTHONPATH and execute pytest
PYTHONPATH=./src pytest -v
```

---

##  Author
- **Tusharkanta** - [GitHub Profile](https://github.com/Tusharkanta407)

*This project is dedicated to mastering the mathematical and practical engineering details of attention mechanisms from the ground up.*