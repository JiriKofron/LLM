# Pattern Relationships Documentation

## Overview
This script demonstrates how patterns in dimensions show relationships between words, illustrating how the model learns to capture different types of relationships through its training.

## Key Concepts

### Relationship Patterns
- Gender pairs (king/queen, man/woman)
- Size pairs (big/small, large/tiny)
- Emotion pairs (happy/sad, angry/calm)
- The model learns to capture these relationships in its dimensions

### Context Effects
- The same word can have different relationships in different contexts
- "Bank" can relate to money or rivers depending on context
- The model learns to capture these contextual relationships
- Relationships are not fixed but context-dependent

### Pattern Recognition
- Similar words have similar patterns in their dimensions
- These patterns emerge from how words are used together
- The model learns these patterns during training
- Patterns help the model understand relationships

## Usage
```python
python pattern_relationships.py
```

## Output
The script will show:
1. How dimensions capture different types of relationships
2. How context affects these relationships
3. Examples of relationship patterns
4. How the model learns these patterns
5. Key points about pattern recognition

## Related Files
- `pattern_relationships.py`: The main script
- `requirements.txt`: Required dependencies

## Further Reading
- [Understanding Word Embeddings](https://www.tensorflow.org/tutorials/text/word_embeddings)
- [BERT Paper](https://arxiv.org/abs/1810.04805) 