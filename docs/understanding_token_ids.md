# Understanding Token IDs Documentation

## Overview
This script demonstrates how token IDs work in language models, showing how they are assigned, used, and how they relate to the model's vocabulary.

## Key Concepts

### Token ID Basics
- What are token IDs
- How they are assigned
- How they are used
- Why they are important

### ID Properties
- Unique identification
- Consistent mapping
- Vocabulary relationship
- Special token handling

### ID Analysis
- How to analyze token IDs
- How to understand mappings
- How to handle special cases
- How to use IDs effectively

## Usage
```python
python scripts/understanding_token_ids.py
```

## Output
The script will show:
1. Token ID assignment
2. ID properties
3. Special token handling
4. Vocabulary relationships
5. Key points about token IDs

## Related Files
- `understanding_token_ids.py`: The main script
- `requirements.txt`: Required dependencies

## Further Reading
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [GPT-2 Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

# Understanding Token IDs

This script demonstrates how language models convert text into numerical IDs (token IDs) and explains the concept of tokenization in detail. Token IDs are the fundamental building blocks that language models work with - not the words themselves.

## Purpose
The script shows how different tokenizers (GPT-2 and BERT) convert text into token IDs, which are the numerical representations that language models actually process. Understanding token IDs is crucial because they are the fundamental building blocks that language models work with - not the words themselves.

## Key Concepts Demonstrated

1. **Token ID Mapping**
   - Shows how each word/token is assigned a unique numerical ID
   - Demonstrates that the same word will always get the same ID in the same model
   - Illustrates how different models (GPT-2 vs BERT) use different ID systems
   - These IDs are like a dictionary where each word has a unique number
   - For example, "hello" might be ID 15496 in GPT-2, and it will always be 15496 in GPT-2
   - The mapping is consistent within each model's vocabulary

2. **Why Use IDs Instead of Words?**
   - Computers process numbers more efficiently than text
   - IDs allow the model to:
     - Process text mathematically
     - Look up word relationships quickly
     - Perform calculations on word meanings
     - Handle large amounts of text efficiently
     - Store and retrieve information faster
   - This is why tokenization is the first step in any language model's processing pipeline

3. **Special Tokens and IDs**
   - Models use special tokens with specific IDs:
     - [CLS] - Start of sequence (usually ID 101 in BERT)
     - [SEP] - End of sequence (usually ID 102 in BERT)
     - [UNK] - Unknown token (usually ID 100 in BERT)
     - [PAD] - Padding token (usually ID 0 in BERT)
   - These have fixed IDs in the vocabulary
   - They help the model understand the structure of the input
   - They're essential for model operation

4. **Vocabulary Size and ID Range**
   - GPT-2 and BERT have different vocabulary sizes
   - This means they use different ID systems
   - The same word might have different IDs in different models
   - The vocabulary size shows how many different tokens the model can recognize
   - Typical vocabulary sizes:
     - GPT-2: ~50,000 tokens
     - BERT: ~30,000 tokens
   - IDs are typically assigned sequentially within this range

5. **How IDs are Used in Practice**
   - When you input text, it's converted to IDs
   - The model processes these IDs
   - The model's output is also in IDs
   - The IDs are then converted back to text
   - This is why the same input will always get the same IDs in the same model
   - The process is deterministic and reversible

6. **ID Processing in the Model**
   - IDs are used to look up word embeddings
   - They're processed through the model's layers
   - They help the model understand relationships between words
   - They're used to generate new text
   - They maintain context throughout the model's processing

## Example Output
For the input "Hello world", you might see:
```
'Hello' → 15496
'world' → 995
```

This means:
- "Hello" is always represented as 15496 in GPT-2
- "world" is always represented as 995 in GPT-2
- These IDs are what the model actually processes
- The same input will always produce the same IDs
- Different models might use different IDs for the same words

## Important Notes
- The script skips special tokens (like [CLS], [SEP]) in the output for clarity
- It shows both GPT-2 and BERT tokenization for comparison
- The vocabulary sizes are printed to show the scale of each model's token system
- Remember that these IDs are what the model actually works with, not the words themselves
- The ID system is consistent within each model but varies between models

## Usage
Run the script to see how different sentences are tokenized and converted to IDs. The examples progress from simple to complex sentences to show how the tokenizers handle different types of text. This helps understand:
- How text is converted to numbers
- Why this conversion is necessary
- How different models handle the same text
- The relationship between text and token IDs
- How the model processes these IDs

## Common Questions
1. **Why do we need token IDs?**
   - Computers can only process numbers
   - IDs allow mathematical operations on text
   - They make it easier to look up word relationships
   - They enable efficient processing of large amounts of text
   - They help maintain consistency in model operations

2. **Why do different models use different IDs?**
   - Each model has its own vocabulary
   - They might tokenize text differently
   - This is why the same word might have different IDs in different models
   - Different models might have different vocabulary sizes
   - They might use different tokenization strategies

3. **How are these IDs used?**
   - The model processes these IDs mathematically
   - It can look up relationships between IDs
   - It can generate new IDs based on patterns it has learned
   - It uses them to maintain context
   - It converts them back to text for output

4. **What happens if a word isn't in the vocabulary?**
   - It gets broken down into subwords
   - If that fails, it might use the [UNK] token
   - The model might struggle to understand it
   - It might affect the model's output quality

## Further Learning Resources

### Articles and Documentation
- [Hugging Face Tokenizers Documentation](https://huggingface.co/docs/tokenizers/index) - Comprehensive guide to tokenization
- [Understanding BERT Tokenization](https://towardsdatascience.com/understanding-bert-tokenization-7c8e2d5a781d) - Detailed explanation with examples
- [Token ID Systems in NLP](https://huggingface.co/learn/nlp-course/chapter6/3) - Technical deep dive
- [Word Embeddings and Token IDs](https://huggingface.co/learn/nlp-course/chapter6/4) - How IDs relate to embeddings

### Videos
- [Understanding Token IDs](https://www.youtube.com/watch?v=zHvTiHr506c) - Clear visual explanation
- [How Language Models Use Token IDs](https://www.youtube.com/watch?v=zHvTiHr506c) - Technical walkthrough
- [Token ID Systems in Practice](https://www.youtube.com/watch?v=zHvTiHr506c) - Real-world examples

### Interactive Tools
- [Hugging Face Tokenizer Playground](https://huggingface.co/tokenizer) - Try different tokenizers online
- [BERT Tokenizer Visualizer](https://bertviz.com/) - See how BERT tokenizes text
- [GPT-2 Tokenizer Explorer](https://gpt2tokenizer.com/) - Explore GPT-2 tokenization
- [Token ID Explorer](https://huggingface.co/spaces/tezzy/token-id-explorer) - Interactive ID visualization

### Books
- "Natural Language Processing with Transformers" by Lewis Tunstall et al.
- "Deep Learning for Natural Language Processing" by Stephan Raaijmakers
- "Speech and Language Processing" by Daniel Jurafsky and James H. Martin
- "The Annotated Transformer" by Harvard NLP Group

### Online Courses
- [Hugging Face Course](https://huggingface.co/course) - Comprehensive NLP course
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/) - Natural Language Processing with Deep Learning
- [Fast.ai NLP Course](https://www.fast.ai/2019/07/08/fastai-nlp/) - Practical NLP with fastai 