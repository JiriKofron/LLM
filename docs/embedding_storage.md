# Embedding Storage Documentation

## Overview
This script demonstrates how embeddings are stored in language models and how they persist between model loads. It shows the relationship between tokens, vocabulary, and embeddings in BERT.

## Key Concepts

### Model Files
- `config.json`: Contains model configuration (embedding size, number of layers, etc.)
- `pytorch_model.bin`: Contains all model parameters, including embeddings
- `vocab.txt`: Contains the vocabulary

### Embedding Storage
- Embeddings are stored as a large matrix in the model file
- Each row corresponds to a token ID
- Each column represents a dimension
- For BERT, this is a matrix of size [vocabulary_size × embedding_dimension]
- For BERT-base, that's roughly [30,000 × 768] numbers

### Persistence
- Embeddings are saved with the model
- They persist between model loads
- You don't need to retrain the model each time
- The model file contains all the learned relationships

## Usage
```python
python embedding_storage.py
```

## Output
The script will show:
1. The structure of model files
2. The shape of the embedding matrix
3. How embeddings persist
4. An example with the word "bank"
5. How to save and load embeddings

## Related Files
- `embedding_storage.py`: The main script
- `requirements.txt`: Required dependencies

## Further Reading
- [BERT Documentation](https://huggingface.co/transformers/model_doc/bert.html)
- [PyTorch Embeddings](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html) 