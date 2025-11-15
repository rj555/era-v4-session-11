# Deployment Guide for HuggingFace Spaces

## Prerequisites

1. A HuggingFace account
2. The trained tokenizer file: `bpe_tokenizer.json`
3. All required Python files

## Steps to Deploy

### 1. Create a New Space

1. Go to [HuggingFace Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Fill in the details:
   - **Space name**: `indian-stock-bpe-tokenizer` (or your preferred name)
   - **SDK**: Select "Gradio"
   - **Hardware**: CPU Basic is sufficient
   - **Visibility**: Public or Private (your choice)

### 2. Upload Files

Upload the following files to your Space:

**Required Files:**
- `app.py` - Main Gradio application
- `bpe_tokenizer.py` - BPE tokenizer implementation
- `bpe_tokenizer.json` - Trained tokenizer model (generated after training)
- `requirements.txt` - Python dependencies
- `README.md` or `README_HF.md` - Documentation

**Optional Files:**
- `train_bpe.py` - Training script (for reference)
- `stock_data.py` - Data collection script (for reference)
- `.gitignore` - Git ignore file

### 3. File Structure in HuggingFace Space

Your Space should have this structure:

```
your-space/
├── app.py                 # Main Gradio app (required)
├── bpe_tokenizer.py       # BPE implementation
├── bpe_tokenizer.json     # Trained model
├── requirements.txt       # Dependencies
├── README.md             # Documentation
└── .gitignore            # Optional
```

### 4. Verify Requirements

Make sure `requirements.txt` includes:
```
gradio>=4.0.0
requests>=2.31.0
typing-extensions>=4.0.0
```

### 5. Update README for HuggingFace

If using `README_HF.md`, rename it to `README.md` in the Space, or copy its content to the Space's README.

### 6. Deploy

1. Commit and push all files to your Space
2. HuggingFace will automatically:
   - Install dependencies from `requirements.txt`
   - Run `app.py`
   - Make your app available at `https://huggingface.co/spaces/your-username/your-space-name`

### 7. Verify Deployment

1. Wait for the build to complete (usually 2-5 minutes)
2. Check the "Logs" tab for any errors
3. Test the app in the "App" tab
4. Verify:
   - Encoding works correctly
   - Decoding works correctly
   - Statistics display properly

## Troubleshooting

### Tokenizer Not Found Error

If you see "Tokenizer not found" error:
1. Ensure `bpe_tokenizer.json` is uploaded to the Space
2. Check file permissions
3. Verify the file path in `app.py` matches the actual file location

### Import Errors

If you see import errors:
1. Check `requirements.txt` includes all dependencies
2. Verify Python version compatibility (HuggingFace uses Python 3.9+)
3. Check the "Logs" tab for detailed error messages

### App Not Loading

If the app doesn't load:
1. Check the "Logs" tab for errors
2. Verify `app.py` has the correct structure
3. Ensure `demo.launch()` is called at the end of `app.py`

## Testing Locally Before Deployment

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure `bpe_tokenizer.json` exists (train if needed):
   ```bash
   python train_bpe.py
   ```

3. Run the app locally:
   ```bash
   python app.py
   ```

4. Test all features:
   - Encode some text
   - Decode token IDs
   - View statistics

## Updating the Space

To update your Space:
1. Make changes to files locally
2. Commit and push to the Space repository
3. HuggingFace will automatically rebuild and redeploy

## Customization

You can customize the app by:
- Modifying the Gradio interface in `app.py`
- Changing the theme or layout
- Adding new features
- Updating the tokenizer (retrain and upload new `bpe_tokenizer.json`)

## Support

For issues or questions:
1. Check the HuggingFace Spaces documentation
2. Review the app logs in the Space
3. Check the GitHub repository (if linked)


