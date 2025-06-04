# Understanding Unknown Words Documentation

## Overview
This script demonstrates how language models handle unknown words, showing different strategies for tokenizing and processing words that aren't in their vocabulary.

## Key Concepts

### Unknown Word Handling
- How models identify unknown words
- Different handling strategies
- Subword tokenization
- Special token usage

### Handling Strategies
- BPE for unknown words
- WordPiece for unknown words
- Character-level fallback
- Special token replacement

### Strategy Analysis
- How to analyze handling
- How to understand strategies
- How to handle special cases
- How to evaluate effectiveness

## Usage
```python
python scripts/understanding_unknown_words.py
```

## Output
The script will show:
1. Unknown word identification
2. Handling strategies
3. Subword tokenization
4. Special token usage
5. Key points about unknown words

## Related Files
- `understanding_unknown_words.py`: The main script
- `requirements.txt`: Required dependencies

## Further Reading
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [GPT-2 Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 