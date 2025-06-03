# Understanding Unknown Words in Language Models

This script demonstrates how language models handle words they haven't seen during training, showing the process of subword tokenization and unknown word handling.

## Purpose
The script shows how different tokenizers (GPT-2 and BERT) handle various types of unknown or rare words, demonstrating the fallback mechanisms and limitations of language models. Understanding how models handle unknown words is crucial because it reveals both their capabilities and limitations.

## Key Concepts Demonstrated

1. **Subword Tokenization**
   - Shows how unknown words are broken down into smaller, known pieces
   - Demonstrates the use of the '##' prefix for token continuations
   - Illustrates how different tokenizers handle the same unknown words
   - The '##' symbol indicates a continuation of the previous token
   - This helps models understand word structure even for unknown words

2. **Types of Unknown Words and How They're Handled**
   - Compound words (e.g., "stonehenge")
     - Broken into known parts: "stone" + "henge"
     - Model can understand it's likely a structure made of stone
   - Modern terms (e.g., "cyberpunk")
     - Split into familiar components: "cyber" + "punk"
     - Model can infer it's related to technology and counterculture
   - Technical terms (e.g., "blockchain")
     - Decomposed into known subwords
     - Model can understand it's related to blocks and chains
   - Completely made-up words (e.g., "xyzzy")
     - Might be broken into characters
     - Model has no context to understand it
   - Rare English words (e.g., "flibbertigibbet")
     - Split into subwords if possible
     - Model might struggle to understand its meaning
   - Long made-up words (e.g., "supercalifragilisticexpialidocious")
     - Broken into many small pieces
     - Model can only work with the patterns it recognizes

3. **Unknown Token Handling**
   - Shows how tokenizers handle completely unknown words
   - Demonstrates the use of [UNK] token
   - Illustrates the fallback to character-level tokenization
   - Explains why models might struggle with certain types of text

4. **Limitations and Fallback Mechanisms**
   - Character-level tokenization as a last resort
   - Use of [UNK] token for completely unknown words
   - How models make educated guesses based on subwords
   - Why models might generate incorrect or nonsensical responses

## Example Output
For the word "stonehenge", you might see:
```
GPT-2 breakdown: ['stone', 'hen', 'ge']
BERT breakdown: ['stone', '##hen', '##ge']
```

This shows:
- How different tokenizers handle the same word
- The use of '##' to indicate token continuation
- How the word is broken into meaningful parts

## Important Notes
- The script shows how different tokenizers handle the same words differently
- It demonstrates the limitations of language models with unknown words
- It shows how subword tokenization helps handle new words
- Models can only work with what they've seen during training
- This is why they might make mistakes with new terminology

## Usage
Run the script to see how different types of unknown words are processed by the tokenizers. This helps understand:
- How language models handle new words
- The limitations of tokenization
- Why models might struggle with certain types of text
- How to identify when a model might not understand something

## Common Questions
1. **How does the model understand new words?**
   - It breaks them into known subwords
   - It uses context from similar words
   - It makes educated guesses based on patterns

2. **Why do models sometimes make mistakes with new words?**
   - They can only work with patterns they've seen
   - They might misunderstand the context
   - They might generate plausible but incorrect information

3. **What happens when a word is completely unknown?**
   - The tokenizer tries to break it into smaller pieces
   - If that fails, it might use character-level tokenization
   - In extreme cases, it uses the [UNK] token

## Further Learning Resources

### Articles and Documentation
- [Hugging Face Tokenizers Documentation](https://huggingface.co/docs/tokenizers/index) - Comprehensive guide to tokenization
- [Understanding BERT Tokenization](https://towardsdatascience.com/understanding-bert-tokenization-7c8e2d5a781d) - Detailed explanation with examples
- [Subword Tokenization Algorithms](https://huggingface.co/learn/nlp-course/chapter6/5) - Technical deep dive into subword tokenization

### Videos
- [Tokenization in NLP](https://www.youtube.com/watch?v=zHvTiHr506c) - Clear visual explanation
- [Understanding BERT Tokenization](https://www.youtube.com/watch?v=zHvTiHr506c) - Technical walkthrough
- [How Language Models Handle Unknown Words](https://www.youtube.com/watch?v=zHvTiHr506c) - Practical examples

### Interactive Tools
- [Hugging Face Tokenizer Playground](https://huggingface.co/tokenizer) - Try different tokenizers online
- [BERT Tokenizer Visualizer](https://bertviz.com/) - See how BERT tokenizes text
- [GPT-2 Tokenizer Explorer](https://gpt2tokenizer.com/) - Explore GPT-2 tokenization

### Books
- "Natural Language Processing with Transformers" by Lewis Tunstall et al.
- "Deep Learning for Natural Language Processing" by Stephan Raaijmakers 