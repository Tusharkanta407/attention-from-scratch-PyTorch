from lotr_transformer.vocab import Vocab
import torch

def test_vocab_basic():
    tokens = ["hello", "world", "hello", "test", "hello"]
    vocab = Vocab(tokens, special_tokens=['<UNK>'], min_freq=1, default_token='<UNK>')
    
    assert vocab.token_to_idx("hello") != vocab.token_to_idx("world")
    assert vocab.token_to_idx("nonexistent") == vocab.token_to_idx("<UNK>")
    assert vocab.idx_to_token(vocab.token_to_idx("hello")) == "hello"

def test_vocab_min_freq():
    tokens = ["apple", "banana", "apple", "cherry"]
    # Cherry and banana appear only once, apple appears twice.
    # If min_freq=2, cherry and banana should be filtered out and fallback to <UNK>.
    vocab = Vocab(tokens, special_tokens=['<UNK>'], min_freq=2, default_token='<UNK>')
    
    assert vocab.token_to_idx("apple") != vocab.token_to_idx("<UNK>")
    assert vocab.token_to_idx("banana") == vocab.token_to_idx("<UNK>")
    assert vocab.token_to_idx("cherry") == vocab.token_to_idx("<UNK>")

def test_vocab_tensor_conversion():
    tokens = ["a", "b", "c"]
    vocab = Vocab(tokens, special_tokens=['<UNK>'], min_freq=1, default_token='<UNK>')
    
    indices = torch.tensor([vocab.token_to_idx(t) for t in ["a", "b", "c"]])
    reconstructed = vocab.idx_tensor_to_tokens(indices)
    assert reconstructed == ["a", "b", "c"]
