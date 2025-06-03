# LLM Learning Project

This project is designed to help understand Large Language Models (LLMs) from the ground up. We'll explore various concepts, implement simple examples, and gradually build up to more complex applications.

## Project Structure

```
.
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── notebooks/               # Jupyter notebooks for interactive learning
│   └── 01_basics.ipynb      # Basic LLM concepts and examples
├── src/                     # Source code
│   ├── __init__.py
│   ├── tokenizer/          # Tokenization examples
│   ├── embeddings/         # Word embeddings and vector representations
│   └── models/            # Simple model implementations
└── examples/              # Example applications
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

3. Start with the notebooks in the `notebooks` directory, beginning with `01_basics.ipynb`

## Resources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original transformer paper
- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) - Visual guide to transformers
- [Hugging Face Course](https://huggingface.co/course) - Practical deep learning for NLP 