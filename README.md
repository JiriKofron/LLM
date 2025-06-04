# Understanding Language Models

This project helps you understand how language models work, from basic concepts to advanced topics.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── docs/
│   ├── ATTENTION_MECHANISMS.md
│   ├── EMBEDDINGS.md
│   ├── TOKENIZATION.md
│   ├── embedding_storage.md
│   ├── dimension_meaning.md
│   ├── pattern_relationships.md
│   ├── training_relationships.md
│   ├── embedding_values.md
│   ├── embedding_dimensions.md
│   ├── token_embedding_relationship.md
│   ├── training_example.md
│   ├── bpe_example.md
│   ├── show_token_mappings.md
│   ├── understanding_token_ids.md
│   ├── understanding_unknown_words.md
│   └── tokenization_demo.md
├── notebooks/
│   └── 01_basic_concepts.ipynb
└── scripts/
    ├── compare_tokenizers.py
    ├── embedding_storage.py
    ├── dimension_meaning.py
    ├── pattern_relationships.py
    ├── training_relationships.py
    ├── embedding_values.py
    ├── embedding_dimensions.py
    ├── token_embedding_relationship.py
    ├── training_example.py
    ├── bpe_example.py
    ├── show_token_mappings.py
    ├── understanding_token_ids.py
    ├── understanding_unknown_words.py
    └── tokenization_demo.py
```

## Documentation

### Core Concepts
- [Tokenization](docs/TOKENIZATION.md) - How text is broken down into tokens
- [Embeddings](docs/EMBEDDINGS.md) - How words are represented as numbers
- [Attention Mechanisms](docs/ATTENTION_MECHANISMS.md) - How models focus on different parts of text

### Tokenization Scripts
- [Tokenization Demo](docs/tokenization_demo.md) - Basic tokenization concepts
- [Understanding Token IDs](docs/understanding_token_ids.md) - How token IDs work
- [Understanding Unknown Words](docs/understanding_unknown_words.md) - How models handle unknown words
- [Show Token Mappings](docs/show_token_mappings.md) - Token to ID mappings
- [BPE Example](docs/bpe_example.md) - Byte-Pair Encoding demonstration

### Embedding Scripts
- [Embedding Storage](docs/embedding_storage.md) - How embeddings are stored
- [Embedding Values](docs/embedding_values.md) - How embedding values work
- [Embedding Dimensions](docs/embedding_dimensions.md) - How dimensions capture meaning
- [Token Embedding Relationship](docs/token_embedding_relationship.md) - How tokens map to embeddings

### Training and Relationships
- [Training Example](docs/training_example.md) - How training affects embeddings
- [Training Relationships](docs/training_relationships.md) - How training influences relationships
- [Pattern Relationships](docs/pattern_relationships.md) - How patterns show relationships
- [Dimension Meaning](docs/dimension_meaning.md) - How dimensions work together

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the scripts:
```bash
# Basic tokenization
python scripts/tokenization_demo.py
python scripts/understanding_token_ids.py
python scripts/understanding_unknown_words.py
python scripts/show_token_mappings.py
python scripts/bpe_example.py

# Embeddings
python scripts/embedding_storage.py
python scripts/embedding_values.py
python scripts/embedding_dimensions.py
python scripts/token_embedding_relationship.py

# Training and relationships
python scripts/training_example.py
python scripts/training_relationships.py
python scripts/pattern_relationships.py
python scripts/dimension_meaning.py
```

3. Open the Jupyter notebook:
```bash
jupyter notebook notebooks/01_basic_concepts.ipynb
```

## Learning Path

1. Start with the basic concepts notebook
2. Read the core concept documentation
3. Run the example scripts in order:
   - Tokenization scripts
   - Embedding scripts
   - Training and relationship scripts
4. Explore the advanced topics

## Resources

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [GPT-2 Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

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