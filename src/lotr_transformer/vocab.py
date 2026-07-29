"""
Vocab utils
Implement <UNK> handling, case-sensitive mapping, and frequency-based filtering.
"""
from typing import List

class Vocab:
    def __init__(self, tokens: List[str], special_tokens: List[str] = ['<UNK>'], min_freq: int = 0, default_token: str = '<UNK>'):
        # TODO: Count token occurrences, filter by min_freq, prepend/append special tokens,
        # and build token-to-index and index-to-token mappings.
        pass

    def idx_to_token(self, i: int) -> str:
        # TODO: Return the token corresponding to the index `i`
        pass

    def idx_tensor_to_tokens(self, indices) -> List[str]:
        # TODO: Convert a list or tensor of indices back into token strings
        pass

    def token_to_idx(self, token: str) -> int:
        # TODO: Return the index for the given token, fallback to default_token if OOV
        pass

    def tokens_to_idx_list(self, text: List[str]) -> List[int]:
        # TODO: Convert a list of token strings into a list of integer indices
        pass

    def __len__(self) -> int:
        # TODO: Return the total number of unique tokens in the vocabulary
        pass
