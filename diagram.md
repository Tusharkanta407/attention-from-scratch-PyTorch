graph TD
    %% Config & Raw Data
    A[configs/default.yaml] -->|Loads YAML dict| B(src/lotr_transformer/config.py)
    C[(raw text: lotr.txt)] -->|Reads corpus| D(src/lotr_transformer/vocab.py)
    
    %% Tokenization and Dataset
    D -->|Builds token <-> idx map| E(src/lotr_transformer/data.py)
    C -->|SpaCy/Unicode tokenization| E
    E -->|Generates batch inputs X & targets Y| F(src/lotr_transformer/train_loop.py)

    %% The Model Architecture
    subgraph Model: src/lotr_transformer/model.py
        G[Token IDs: B, S] -->|ScaledEmbedding| H[Embeddings: B, S, d_model]
        H -->|PositionalEncoding| I[Positional Embeddings: B, S, d_model]
        I -->|Causal Mask| J[N x DecoderLayer: src/lotr_transformer/layers.py]
        
        subgraph Decoder Layer Block
            J -->|Multi-Head Self-Attention| K[src/lotr_transformer/attention.py]
            K -->|Residual + LayerNorm| L[Feed Forward Network]
            L -->|Residual + LayerNorm| M[Layer Output]
        end
        
        M -->|Linear LM Head| N[Logits: B, S, vocab_size]
    end

    F -->|Feeds batches| G
    N -->|Cross-Entropy Loss with Label Smoothing| F
