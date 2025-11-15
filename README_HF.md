---
title: Indian Stock Market BPE Tokenizer
emoji: 🇮🇳
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# Indian Stock Market BPE Tokenizer

A Byte-Pair Encoding (BPE) tokenizer trained specifically on Indian stock market data from NSE (National Stock Exchange) and BSE (Bombay Stock Exchange).

## Features

- ✅ **Vocabulary Size**: 5,500 tokens (exceeds 5,000 requirement)
- ✅ **Compression Ratio**: 9.66x (exceeds 3.0 requirement)
- ✅ **Optimized for**: Indian stock market terminology, ticker symbols, and financial terms

## Usage

1. **Encode**: Enter text to see tokenization (e.g., "Buy RELIANCE stock on NSE")
2. **Decode**: Enter token IDs to reconstruct text
3. **Statistics**: View tokenizer statistics and vocabulary information

## Requirements Met

- ✅ More than 5,000 tokens in vocabulary
- ✅ Compression ratio of 3.0 or above (achieved 9.66x)

## Files

- `app.py` - Gradio application
- `bpe_tokenizer.py` - BPE tokenizer implementation
- `bpe_tokenizer.json` - Trained tokenizer model
- `requirements.txt` - Python dependencies

## Training

The tokenizer was trained on a comprehensive corpus of:
- NSE and BSE stock ticker symbols
- Company names and abbreviations
- Financial terms and metrics
- Market-related terminology
- Trading terms and concepts

## License

MIT License


