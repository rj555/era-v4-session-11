# Quick Start Guide

## ✅ Requirements Met

- ✅ **Vocabulary Size**: 5,500 tokens (exceeds 5,000 requirement)
- ✅ **Compression Ratio**: 9.66x (exceeds 3.0 requirement)

## 🚀 Quick Start

### 1. Train the Tokenizer (Already Done)

The tokenizer has been trained and saved to `bpe_tokenizer.json`. If you need to retrain:

```bash
python train_bpe.py
```

### 2. Run the Gradio App Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at `http://localhost:7860`

### 3. Deploy to HuggingFace Spaces

1. Create a new Space on HuggingFace
2. Upload these files:
   - `app.py`
   - `bpe_tokenizer.py`
   - `bpe_tokenizer.json`
   - `requirements.txt`
   - `README.md` or `README_HF.md`
3. HuggingFace will automatically deploy your app

See `DEPLOYMENT.md` for detailed deployment instructions.

## 📊 Tokenizer Performance

- **Vocabulary Size**: 5,500 tokens
- **Compression Ratio**: 9.66x
- **Training Data**: 434,040 entries (21,903 unique)
- **Coverage**: NSE and BSE stock symbols, company names, financial terms

## 🔍 Example Usage

### Python API

```python
from bpe_tokenizer import BPETokenizer

# Load tokenizer
tokenizer = BPETokenizer()
tokenizer.load("bpe_tokenizer.json")

# Encode
text = "Buy RELIANCE stock on NSE"
token_ids = tokenizer.encode(text)
print(f"Token IDs: {token_ids}")
# Output: [160, 1825, 485, 80, 496]

# Decode
decoded = tokenizer.decode(token_ids)
print(f"Decoded: {decoded}")
# Output: Buy RELIANCE stock on NSE
```

### Gradio App

1. **Encode Tab**: Enter text to see tokenization
2. **Decode Tab**: Enter token IDs to reconstruct text
3. **Statistics Tab**: View tokenizer statistics

## 📁 File Structure

```
.
├── app.py                 # Gradio application
├── bpe_tokenizer.py       # BPE tokenizer implementation
├── bpe_tokenizer.json     # Trained tokenizer model
├── train_bpe.py          # Training script
├── stock_data.py         # Data collection script
├── requirements.txt      # Python dependencies
├── README.md             # Main documentation
├── README_HF.md          # HuggingFace Spaces README
├── DEPLOYMENT.md         # Deployment guide
└── QUICKSTART.md         # This file
```

## 🎯 Key Features

1. **High Compression**: Achieves 9.66x compression ratio
2. **Large Vocabulary**: 5,500 tokens for comprehensive coverage
3. **Domain-Specific**: Optimized for Indian stock market data
4. **Interactive Demo**: Gradio app for easy testing
5. **Deployable**: Ready for HuggingFace Spaces deployment

## 🔧 Troubleshooting

### Tokenizer Not Found
- Ensure `bpe_tokenizer.json` exists in the same directory
- Run `python train_bpe.py` to generate it

### Import Errors
- Install dependencies: `pip install -r requirements.txt`
- Check Python version (3.7+)

### App Not Loading
- Check if Gradio is installed: `pip install gradio`
- Verify `app.py` is in the correct directory
- Check console for error messages

## 📚 Documentation

- `README.md` - Main documentation
- `DEPLOYMENT.md` - Deployment instructions
- `README_HF.md` - HuggingFace Spaces documentation

## 📝 Notes

- The tokenizer is optimized for Indian stock market terminology
- It may not work optimally for general text
- Compression ratio is calculated as: characters / tokens
- Higher compression means fewer tokens per character


