# Indian Stock Market BPE Tokenizer

A Byte-Pair Encoding (BPE) tokenizer trained specifically on Indian stock market data from NSE (National Stock Exchange) and BSE (Bombay Stock Exchange).

## Features

- **Vocabulary Size**: 5,500 tokens
- **Compression Ratio**: 9.69x
- **Optimized for**: Indian stock market terminology, ticker symbols, and financial terms

## Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Training the Tokenizer

Train the BPE tokenizer on Indian stock market data:

```bash
python train_bpe.py
```

This will:
1. Generate a corpus of Indian stock market data (NSE and BSE)
2. Train the BPE tokenizer to achieve 5,500 vocabulary size
3. Calculate and verify compression ratio (achieved: 9.69x)
4. Save the tokenizer to `bpe_tokenizer.json`

## Usage

### Python API

```python
from bpe_tokenizer import BPETokenizer

# Load trained tokenizer
tokenizer = BPETokenizer()
tokenizer.load("bpe_tokenizer.json")

# Encode text
text = "Buy RELIANCE stock on NSE"
token_ids = tokenizer.encode(text)
print(f"Token IDs: {token_ids}")

# Decode tokens
decoded = tokenizer.decode(token_ids)
print(f"Decoded: {decoded}")
```

### Gradio App

Run the interactive Gradio app:

```bash
python app.py
```

The app provides:
- **Encode**: Tokenize input text and view token IDs
- **Decode**: Convert token IDs back to text
- **Statistics**: View tokenizer statistics and vocabulary information

## Deployment to HuggingFace Spaces

1. Create a new Space on HuggingFace
2. Upload all files to the Space
3. Ensure `bpe_tokenizer.json` is included (trained model)
4. The app will automatically load the tokenizer on startup

### Files for HuggingFace

- `app.py` - Gradio application
- `bpe_tokenizer.py` - BPE tokenizer implementation
- `bpe_tokenizer.json` - Trained tokenizer (generated after training)
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Statistics

After training, the tokenizer should achieve:
- Vocabulary size: 5,500 tokens
- Compression ratio: 9.69x

## License

See LICENSE file for details.
