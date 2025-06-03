# LLM Learning Project

This project is designed to help understand Large Language Models (LLMs) from the ground up. We'll explore various concepts, implement simple examples, and gradually build up to more complex applications.

## Important Note
The user runs scripts in a separate terminal. Please refer to `CONTEXT.md` for additional context and preferences.

## Project Structure

```
.
├── README.md                 # This file
├── CONTEXT.md               # Project context and preferences
├── requirements.txt          # Python dependencies
├── show_token_mappings.py    # Demonstrates token ID mappings
└── compare_tokenizers.py     # Compares different tokenization approaches
```

## Learning Path

1. **Basics of Language Models**
   - What are Language Models?
   - Tokenization
   - Word embeddings
   - Basic probability and prediction

2. **Transformer Architecture**
   - Attention mechanisms
   - Self-attention
   - Positional encoding
   - Feed-forward networks

3. **Training and Fine-tuning**
   - Pre-training
   - Fine-tuning
   - Prompt engineering
   - Few-shot learning

4. **Applications**
   - Text generation
   - Question answering
   - Text classification
   - Code generation

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Resources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original transformer paper
- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) - Visual guide to transformers
- [Hugging Face Course](https://huggingface.co/course) - Practical deep learning for NLP

# BERT vs GPT-2 Tokenizer Comparison

This project demonstrates the differences between BERT and GPT-2 tokenization approaches, helping to understand why these models use different tokenization strategies despite both being based on subword tokenization.

## Key Differences

### Vocabulary Size
- GPT-2: ~50,000 tokens
- BERT: ~30,000 tokens

### Tokenization Methods
- GPT-2: Uses Byte-Pair Encoding (BPE)
- BERT: Uses WordPiece tokenization

### Design Goals
- GPT-2: Optimized for text generation
- BERT: Optimized for understanding tasks

## Running the Comparison

1. Run the comparison script:
```bash
python compare_tokenizers.py
```

2. Run the token mapping demonstration:
```bash
python show_token_mappings.py
```

## What to Look For

The scripts will show you:
1. How each tokenizer breaks down different types of text
2. The number of tokens used by each approach
3. How they handle technical terms and subwords
4. The differences in token IDs

## Common Questions

### Why does GPT-2 use more tokens?
- Larger vocabulary helps with text generation
- More direct word representations
- Better handling of diverse vocabulary

### Why does BERT use fewer tokens?
- More efficient for understanding tasks
- Better at handling technical terms
- More focused on common subwords

### Which is better?
- Neither is inherently better
- Depends on the task:
  - GPT-2's approach is better for generation
  - BERT's approach is better for understanding

## Further Learning

1. Read the original papers:
   - BERT: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
   - GPT-2: "Language Models are Unsupervised Multitask Learners"

2. Explore the tokenizers:
   - GPT-2: https://huggingface.co/gpt2
   - BERT: https://huggingface.co/bert-base-uncased

3. Try different types of text to see how they handle:
   - Technical terms
   - Slang and informal language
   - Domain-specific vocabulary 