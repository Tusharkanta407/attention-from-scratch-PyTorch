"""
Vocab utils
Implement <UNK> handling, case-sensitive mapping, and frequency-based filtering.
"""
from typing import List

class Vocab:
    def __init__(self, tokens: List[str], special_tokens: List[str] = ['<UNK>'], min_freq: int = 0, default_token: str = '<UNK>'):
        counter:collections.Counter=collections.Counter()
        counter.update(tokens)
        self.vocab_list:List[str]=[token for token,count in counter.items() if count >=min_freq]
        if default_token not in special_tokens:
            special_tokens.append(default_token)
        self.vocab_list+=special_tokens
        self.vocab_dict={token:i for i,token in enumerate(self.vocab_list)}
        self.default_idx=self.vocab_dict[default_token]

    def idx_to_token(self, i: int) -> str:
        return self.vocab_list[i]

    def idx_tensor_to_tokens(self, indices) -> List[str]:
        return [self.vocab_list[i.item()] for i in indices]

    def token_to_idx(self, token: str) -> int:
        return self.vocab_dict.get(token,self.default_idx)

    def tokens_to_idx_list(self, text: List[str]) -> List[int]:
        return [self.token_to_idx(token) for token in text]

    def __len__(self) -> int:
        return len(self.vocab_list)
