"""
Byte-Pair Encoding (BPE) Tokenizer for Indian Stock Market Data
"""

from collections import defaultdict, Counter
from typing import List, Dict, Tuple
import re


class BPETokenizer:
    """Byte-Pair Encoding tokenizer implementation"""
    
    def __init__(self, vocab_size: int = 5000):
        self.vocab_size = vocab_size
        self.vocab = {}  # token_id -> token
        self.merges = []  # List of merge rules (pair, new_token_id)
        self.word_freqs = {}
        
    def _get_word_freqs(self, corpus: List[str]) -> Dict[str, int]:
        """Calculate word frequencies from corpus"""
        word_freqs = defaultdict(int)
        for text in corpus:
            # Split by whitespace and count frequencies
            words = text.split()
            for word in words:
                word_freqs[word] += 1
        return dict(word_freqs)
    
    def _get_stats(self, vocab: Dict[str, int]) -> Dict[Tuple[str, str], int]:
        """Get statistics of pairs in the vocabulary"""
        pairs = defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pairs[(symbols[i], symbols[i + 1])] += freq
        return pairs
    
    def _merge_vocab(self, pair: Tuple[str, str], vocab: Dict[str, int]) -> Dict[str, int]:
        """Merge the most frequent pair in the vocabulary"""
        bigram = re.escape(' '.join(pair))
        p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
        new_vocab = {}
        for word in vocab:
            new_word = p.sub(''.join(pair), word)
            new_vocab[new_word] = vocab[word]
        return new_vocab
    
    def train(self, corpus: List[str]):
        """Train the BPE tokenizer on the corpus"""
        print(f"Training BPE tokenizer to {self.vocab_size} tokens...")
        
        # Get word frequencies
        self.word_freqs = self._get_word_freqs(corpus)
        print(f"Found {len(self.word_freqs)} unique words")
        
        # Initialize vocabulary with all characters
        vocab = {}
        for word, freq in self.word_freqs.items():
            # Represent each word as a sequence of characters separated by spaces
            # Add special end-of-word token
            word_chars = ' '.join(list(word)) + ' </w>'
            vocab[word_chars] = freq
        
        # Build base vocabulary from all unique characters
        chars = set()
        for word in vocab.keys():
            chars.update(word.split())
        
        # Initialize token to id mapping
        self.vocab = {char: idx for idx, char in enumerate(sorted(chars))}
        num_merges = self.vocab_size - len(self.vocab)
        
        print(f"Starting with {len(self.vocab)} base tokens")
        print(f"Will perform {num_merges} merges...")
        
        # Perform merges
        for i in range(num_merges):
            pairs = self._get_stats(vocab)
            if not pairs:
                break
                
            # Get most frequent pair
            best_pair = max(pairs, key=pairs.get)
            vocab = self._merge_vocab(best_pair, vocab)
            
            # Add new token to vocabulary
            new_token = ''.join(best_pair)
            new_token_id = len(self.vocab)
            self.vocab[new_token] = new_token_id
            self.merges.append((best_pair, new_token_id))
            
            if (i + 1) % 100 == 0:
                print(f"  Merge {i + 1}/{num_merges}: {best_pair} -> {new_token} (vocab size: {len(self.vocab)})")
        
        print(f"Training complete! Final vocabulary size: {len(self.vocab)}")
        return self
    
    def _apply_bpe(self, word: str) -> List[str]:
        """Apply BPE encoding to a single word"""
        if word not in self.word_freqs:
            # For unknown words, use character-level encoding
            word = ' '.join(list(word)) + ' </w>'
        else:
            # Start with character-level representation
            word = ' '.join(list(word)) + ' </w>'
        
        # Apply all merge rules
        for pair, _ in self.merges:
            bigram = re.escape(' '.join(pair))
            p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
            word = p.sub(''.join(pair), word)
        
        return word.split()
    
    def encode(self, text: str) -> List[int]:
        """Encode text into token IDs"""
        words = text.split()
        token_ids = []
        for word in words:
            tokens = self._apply_bpe(word)
            for token in tokens:
                if token in self.vocab:
                    token_ids.append(self.vocab[token])
                else:
                    # Handle unknown tokens (fallback to character encoding)
                    for char in token:
                        if char in self.vocab:
                            token_ids.append(self.vocab[char])
        return token_ids
    
    def decode(self, token_ids: List[int]) -> str:
        """Decode token IDs back to text"""
        # Reverse vocab mapping
        id_to_token = {v: k for k, v in self.vocab.items()}
        tokens = [id_to_token.get(id, '<UNK>') for id in token_ids]
        # Remove </w> markers and join
        text = ''.join(tokens).replace('</w>', ' ').strip()
        return text
    
    def get_compression_ratio(self, texts: List[str]) -> float:
        """Calculate compression ratio: original_size / tokenized_size"""
        total_original = 0
        total_tokenized = 0
        
        for text in texts:
            # Original size in characters
            original_size = len(text)
            # Tokenized size (number of tokens)
            token_ids = self.encode(text)
            tokenized_size = len(token_ids)
            
            total_original += original_size
            total_tokenized += tokenized_size
        
        if total_tokenized == 0:
            return 0.0
        
        compression_ratio = total_original / total_tokenized
        return compression_ratio
    
    def save(self, filepath: str):
        """Save tokenizer to file"""
        import json
        with open(filepath, 'w') as f:
            json.dump({
                'vocab': self.vocab,
                'merges': self.merges,
                'vocab_size': self.vocab_size,
                'word_freqs': dict(list(self.word_freqs.items())[:1000])  # Save sample
            }, f, indent=2)
    
    def load(self, filepath: str):
        """Load tokenizer from file"""
        import json
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.vocab = data['vocab']
            self.merges = data['merges']
            self.vocab_size = data['vocab_size']
            self.word_freqs = data.get('word_freqs', {})


