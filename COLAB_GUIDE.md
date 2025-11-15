# Google Colab Training Notebook Guide

## Overview

The `BPE_Tokenizer_Training.ipynb` notebook provides a complete training pipeline for the Indian Stock Market BPE Tokenizer in Google Colab.

## Quick Start

### 1. Open in Google Colab

1. Upload `BPE_Tokenizer_Training.ipynb` to Google Colab
2. Or open directly from GitHub (if uploaded)
3. Click "Run all" or run cells sequentially

### 2. Notebook Structure

The notebook is organized into the following sections:

1. **Setup** - Install dependencies
2. **BPE Tokenizer Implementation** - Complete tokenizer class
3. **Stock Data Collection** - Functions to collect NSE/BSE data
4. **Generate Corpus** - Create training corpus
5. **Train Tokenizer** - Train BPE tokenizer
6. **Verify Requirements** - Check vocabulary size and compression ratio
7. **Test Examples** - Test tokenizer with sample texts
8. **Save Tokenizer** - Save trained model
9. **Download** - Download tokenizer to local machine
10. **Visualization** (Optional) - Visualize statistics
11. **Summary** - Final results and next steps

### 3. Running the Notebook

#### Option A: Run All Cells
- Click `Runtime` → `Run all`
- Wait for training to complete (takes ~2-5 minutes)

#### Option B: Run Cell by Cell
1. Run cells in order from top to bottom
2. Each cell builds on the previous one
3. Review outputs at each step

### 4. Expected Outputs

#### Vocabulary Size
- Target: > 5,000 tokens
- Expected: ~5,500 tokens
- Status: ✅ PASSED

#### Compression Ratio
- Target: >= 3.0x
- Expected: ~9.66x
- Status: ✅ PASSED

### 5. Downloading the Tokenizer

After training completes:
1. Run the download cell (Cell 8)
2. The file `bpe_tokenizer.json` will download to your local machine
3. Alternatively, use Colab's file browser to download

### 6. Using the Trained Tokenizer

```python
from bpe_tokenizer import BPETokenizer

# Load tokenizer
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

## Troubleshooting

### Issue: Import Error
**Solution**: Run the installation cell first
```python
!pip install -q typing-extensions
```

### Issue: Out of Memory
**Solution**: Reduce corpus size or use a smaller vocabulary size
```python
target_vocab_size = 5000  # Instead of 5500
```

### Issue: Download Not Working
**Solution**: 
1. Check if file exists: `!ls -lh bpe_tokenizer.json`
2. Use Colab file browser to download manually
3. Or use: `from google.colab import files; files.download('bpe_tokenizer.json')`

### Issue: Training Takes Too Long
**Solution**:
1. Reduce vocabulary size
2. Reduce corpus repetition (change `* 15` to `* 10`)
3. Use a smaller sample for testing

## Customization

### Change Vocabulary Size
```python
target_vocab_size = 6000  # Increase to 6000 tokens
tokenizer = BPETokenizer(vocab_size=target_vocab_size)
```

### Modify Corpus
Edit the `generate_stock_corpus()` function to:
- Add more stock symbols
- Include additional financial terms
- Change repetition factor

### Adjust Training Parameters
Modify the training cell to:
- Change merge frequency reporting
- Adjust test sample size
- Modify compression ratio calculation

## Next Steps

After training:
1. **Test the tokenizer** with your own stock market data
2. **Deploy to HuggingFace Spaces** using the Gradio app
3. **Integrate into your pipeline** for stock analysis
4. **Extend the vocabulary** with domain-specific terms

## Resources

- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [BPE Tokenization Guide](https://huggingface.co/learn/nlp-course/chapter6/5)
- [Indian Stock Market Data](https://www.nseindia.com/)

## Support

For issues or questions:
1. Check the notebook outputs for error messages
2. Review the troubleshooting section
3. Verify all dependencies are installed
4. Check Colab runtime settings

---

**Happy Training! 🚀**


