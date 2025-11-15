"""
Train BPE tokenizer on Indian stock market data
"""

from bpe_tokenizer import BPETokenizer
from stock_data import generate_stock_corpus, save_corpus
import json


def main():
    print("=" * 60)
    print("Indian Stock Market BPE Tokenizer Training")
    print("=" * 60)
    
    # Generate corpus
    corpus = generate_stock_corpus()
    save_corpus(corpus, "stock_corpus.txt")
    
    # Train tokenizer with target of 5000+ tokens
    # We'll train to 5500 to ensure we exceed 5000
    target_vocab_size = 5500
    tokenizer = BPETokenizer(vocab_size=target_vocab_size)
    
    # Train
    tokenizer.train(corpus)
    
    # Verify vocabulary size
    vocab_size = len(tokenizer.vocab)
    print(f"\n{'='*60}")
    print(f"Vocabulary Size: {vocab_size}")
    print(f"Target: >5000 tokens")
    print(f"Status: {'✓ PASSED' if vocab_size > 5000 else '✗ FAILED'}")
    
    # Calculate compression ratio
    # Use a sample of the corpus for testing
    test_samples = corpus[:1000]  # Use first 1000 samples
    compression_ratio = tokenizer.get_compression_ratio(test_samples)
    
    print(f"\n{'='*60}")
    print(f"Compression Ratio: {compression_ratio:.2f}")
    print(f"Target: >= 3.0")
    print(f"Status: {'✓ PASSED' if compression_ratio >= 3.0 else '✗ FAILED'}")
    
    # Save tokenizer
    tokenizer.save("bpe_tokenizer.json")
    print(f"\n{'='*60}")
    print("Tokenizer saved to bpe_tokenizer.json")
    
    # Show some examples
    print(f"\n{'='*60}")
    print("Example Encodings:")
    print(f"{'='*60}")
    
    test_texts = [
        "RELIANCE NSE",
        "Buy TCS stock",
        "HDFC Bank BSE",
        "National Stock Exchange",
        "Market Capitalization"
    ]
    
    for text in test_texts:
        token_ids = tokenizer.encode(text)
        decoded = tokenizer.decode(token_ids)
        print(f"\nText: '{text}'")
        print(f"Tokens: {token_ids}")
        print(f"Token count: {len(token_ids)}")
        print(f"Character count: {len(text)}")
        print(f"Compression: {len(text) / len(token_ids):.2f}x")
        print(f"Decoded: '{decoded}'")
    
    print(f"\n{'='*60}")
    print("Training Complete!")
    print(f"{'='*60}")
    
    return tokenizer


if __name__ == "__main__":
    tokenizer = main()


