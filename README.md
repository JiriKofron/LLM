# Understanding Language Models

This project helps you understand how language models work, from basic concepts to advanced topics. It provides hands-on examples and detailed documentation to explore different aspects of language models.

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

## Learning Path

1. Start with the core concept documentation
2. Run the example scripts in order:
   - Tokenization scripts
   - Embedding scripts
   - Training and relationship scripts
3. Explore the advanced topics

## Resources

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [GPT-2 Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Byte-Pair Encoding Paper](https://arxiv.org/abs/1508.07909) 