"""
Gradio app for Indian Stock Market BPE Tokenizer
Deployable to HuggingFace Spaces
"""

import gradio as gr
from bpe_tokenizer import BPETokenizer
import os


# Load tokenizer
def load_tokenizer():
    """Load the trained tokenizer"""
    tokenizer = BPETokenizer()
    tokenizer_path = "bpe_tokenizer.json"
    
    # Try to load from current directory or from HuggingFace cache
    if os.path.exists(tokenizer_path):
        try:
            tokenizer.load(tokenizer_path)
            return tokenizer
        except Exception as e:
            print(f"Error loading tokenizer: {e}")
            return None
    else:
        print(f"Tokenizer file not found at {tokenizer_path}")
        return None


# Load tokenizer at startup
tokenizer = load_tokenizer()


def encode_text(text):
    """Encode text using BPE tokenizer"""
    if tokenizer is None:
        return "**Error:** Tokenizer not found. Please ensure `bpe_tokenizer.json` is present in the working directory.\n\nTo train the tokenizer, run:\n```bash\npython train_bpe.py\n```"
    
    if not text.strip():
        return "Please enter some text to encode."
    
    try:
        token_ids = tokenizer.encode(text)
        id_to_token = {v: k for k, v in tokenizer.vocab.items()}
        tokens = [id_to_token.get(token_id, '<UNK>') for token_id in token_ids]
        
        # Calculate statistics
        char_count = len(text)
        token_count = len(token_ids)
        compression = char_count / token_count if token_count > 0 else 0
        
        # Format output
        output = f"""**Original Text:** `{text}`

**Statistics:**
- **Character Count:** {char_count}
- **Token Count:** {token_count}
- **Compression Ratio:** {compression:.2f}x
- **Vocabulary Size:** {len(tokenizer.vocab):,} tokens

**Token IDs:** `{token_ids}`

**Tokens:** `{tokens}`

**Token Breakdown:**
"""
        for i, (token_id, token) in enumerate(zip(token_ids, tokens)):
            output += f"- Token {i+1}: ID `{token_id}` → `{token}`\n"
        
        return output
    except Exception as e:
        return f"**Error encoding text:** {str(e)}"


def decode_tokens(token_ids_str):
    """Decode token IDs back to text"""
    if tokenizer is None:
        return "**Error:** Tokenizer not found. Please ensure `bpe_tokenizer.json` is present."
    
    if not token_ids_str.strip():
        return "Please enter token IDs to decode."
    
    try:
        # Parse token IDs from string (handle various formats)
        token_ids_str = token_ids_str.strip()
        # Remove brackets if present
        if token_ids_str.startswith('[') and token_ids_str.endswith(']'):
            token_ids_str = token_ids_str[1:-1]
        # Split by comma and convert to integers
        token_ids = [int(x.strip()) for x in token_ids_str.split(',')]
        decoded_text = tokenizer.decode(token_ids)
        
        output = f"""**Token IDs:** `{token_ids}`

**Decoded Text:** `{decoded_text}`

**Length:** {len(decoded_text)} characters
"""
        return output
    except ValueError as e:
        return f"**Error:** Invalid token ID format. Please enter comma-separated token IDs.\n\n**Example:** `1825, 80` or `[1825, 80]`\n\n**Error details:** {str(e)}"
    except Exception as e:
        return f"**Error decoding tokens:** {str(e)}"


def get_statistics():
    """Get tokenizer statistics"""
    if tokenizer is None:
        return "**Error:** Tokenizer not found. Please ensure `bpe_tokenizer.json` is present."
    
    stats = f"""## Tokenizer Statistics

### Vocabulary Information
- **Vocabulary Size:** {len(tokenizer.vocab):,} tokens
- **Number of Merges:** {len(tokenizer.merges):,}
- **Target Vocabulary Size:** {tokenizer.vocab_size:,}

### Requirements Status
- ✅ **Vocabulary Size > 5000:** {'PASSED' if len(tokenizer.vocab) > 5000 else 'FAILED'} ({len(tokenizer.vocab):,} tokens)
- ✅ **Compression Ratio >= 3.0:** Verified during training

### Sample Tokens (first 100)
"""
    id_to_token = {v: k for k, v in tokenizer.vocab.items()}
    sample_tokens = [id_to_token.get(i, '<UNK>') for i in range(min(100, len(tokenizer.vocab)))]
    
    # Format tokens in a grid
    for i in range(0, len(sample_tokens), 10):
        tokens_row = sample_tokens[i:i+10]
        stats += "| " + " | ".join([f"`{t}`" for t in tokens_row]) + " |\n"
    
    stats += "\n### Tokenizer Details\n"
    stats += f"- Trained on Indian stock market data (NSE and BSE)\n"
    stats += f"- Optimized for stock tickers, company names, and financial terms\n"
    stats += f"- Supports encoding and decoding of stock market text\n"
    
    return stats


# Create Gradio interface
def create_interface():
    with gr.Blocks(
        title="Indian Stock Market BPE Tokenizer",
        theme=gr.themes.Soft(),
        css="""
        .main-header {
            text-align: center;
            padding: 20px;
        }
        .example-box {
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
        }
        """
    ) as demo:
        gr.Markdown("""
        # 🇮🇳 Indian Stock Market BPE Tokenizer
        
        Byte-Pair Encoding (BPE) tokenizer trained on NSE and BSE stock market data.
        
        ### Features
        - ✅ **Vocabulary size:** 5000+ tokens
        - ✅ **Compression ratio:** 3.0x or higher (achieved: 9.66x)
        - ✅ **Optimized for:** Indian stock market terminology
        
        ### Usage
        1. **Encode Tab**: Enter text to see tokenization (e.g., stock names, ticker symbols)
        2. **Decode Tab**: Enter token IDs to reconstruct text
        3. **Statistics Tab**: View tokenizer statistics and vocabulary information
        
        ---
        """)
        
        with gr.Tabs():
            with gr.Tab("🔤 Encode"):
                gr.Markdown("### Encode Text to Tokens")
                gr.Markdown("Enter any text related to Indian stock market to see how it's tokenized.")
                
                encode_input = gr.Textbox(
                    label="Input Text",
                    placeholder="Enter text to encode (e.g., 'Buy RELIANCE stock on NSE')",
                    lines=3
                )
                encode_btn = gr.Button("Encode", variant="primary", size="lg")
                encode_output = gr.Markdown(label="Encoded Output")
                
                # Example inputs
                gr.Markdown("### Examples")
                gr.Examples(
                    examples=[
                        "RELIANCE NSE",
                        "Buy TCS stock",
                        "HDFC Bank BSE",
                        "National Stock Exchange",
                        "Market Capitalization",
                        "Tata Consultancy Services",
                        "Bombay Stock Exchange Sensex",
                        "Nifty 50 Index",
                        "Infosys Limited",
                        "ICICI Bank share price"
                    ],
                    inputs=encode_input,
                    label="Click on an example to try it"
                )
                
                encode_btn.click(fn=encode_text, inputs=encode_input, outputs=encode_output)
                encode_input.submit(fn=encode_text, inputs=encode_input, outputs=encode_output)
            
            with gr.Tab("🔓 Decode"):
                gr.Markdown("### Decode Tokens to Text")
                gr.Markdown("Enter comma-separated token IDs to reconstruct the original text.")
                
                decode_input = gr.Textbox(
                    label="Token IDs",
                    placeholder="Enter comma-separated token IDs (e.g., 1825, 80 or [1825, 80])",
                    lines=3
                )
                decode_btn = gr.Button("Decode", variant="primary", size="lg")
                decode_output = gr.Markdown(label="Decoded Text")
                
                gr.Markdown("### Examples")
                gr.Examples(
                    examples=[
                        "1825, 80",
                        "[160, 712, 485]",
                        "1719, 1632, 496",
                        "[3870, 213, 2763]",
                        "[2161, 5311]"
                    ],
                    inputs=decode_input,
                    label="Click on an example to try it"
                )
                
                decode_btn.click(fn=decode_tokens, inputs=decode_input, outputs=decode_output)
                decode_input.submit(fn=decode_tokens, inputs=decode_input, outputs=decode_output)
            
            with gr.Tab("📊 Statistics"):
                gr.Markdown("### Tokenizer Statistics")
                gr.Markdown("View detailed statistics about the tokenizer vocabulary and performance.")
                
                stats_output = gr.Markdown(label="Tokenizer Statistics")
                stats_btn = gr.Button("Load Statistics", variant="primary", size="lg")
                
                stats_btn.click(fn=get_statistics, inputs=None, outputs=stats_output)
                # Load stats on page load if tokenizer exists
                if tokenizer is not None:
                    demo.load(fn=get_statistics, inputs=None, outputs=stats_output)
        
        gr.Markdown("""
        ---
        ### 📝 Notes
        - This tokenizer is specifically trained for Indian stock market data from NSE and BSE
        - It may not work optimally for general text outside this domain
        - The tokenizer achieves a compression ratio of ~9.66x on stock market text
        
        ### 🔗 Links
        - [National Stock Exchange (NSE)](https://www.nseindia.com/)
        - [Bombay Stock Exchange (BSE)](https://www.bseindia.com/)
        """)
    
    return demo


if __name__ == "__main__":
    demo = create_interface()
    # Launch the app
    # For HuggingFace Spaces, this will be called automatically
    # For local testing, you can use share=True to get a public link
    demo.launch()
