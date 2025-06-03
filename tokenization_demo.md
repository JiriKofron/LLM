# Basic Tokenization Demo

This script provides a fundamental introduction to tokenization in language models, showing how text is processed before being fed into the model. Tokenization is the first and crucial step in any language model's processing pipeline.

## Purpose
The script demonstrates the basic process of tokenization using two popular language models (GPT-2 and BERT), showing how they convert text into a format that can be processed by the model. Understanding this process is essential because it's the foundation of how language models work with text.

## Key Concepts Demonstrated

1. **Basic Tokenization**
   - Shows how text is broken down into tokens
   - Demonstrates the conversion from text to token IDs
   - Illustrates how tokens can be converted back to text
   - Explains why this conversion is necessary
   - Shows how punctuation and special characters are handled

2. **Different Tokenizer Approaches**
   - GPT-2 tokenization method
     - Uses Byte-Pair Encoding (BPE)
     - Good for general text
     - Handles common words well
   - BERT tokenization method
     - Uses WordPiece tokenization
     - Better for technical text
     - Handles subwords effectively
   - Comparison of the two approaches
     - Different vocabulary sizes
     - Different tokenization strategies
     - Different use cases

3. **Token ID System**
   - How text is converted to numerical IDs
   - How these IDs are used by the model
   - The relationship between tokens and IDs
   - Why numerical representation is necessary
   - How the model processes these IDs

4. **Special Tokens**
   - [CLS] - Start of sequence
   - [SEP] - End of sequence
   - [PAD] - Padding token
   - [UNK] - Unknown token
   - How these special tokens are used

## Example Output
For the input "Hello! This is a test of tokenization.", you might see:
```
Original text: Hello! This is a test of tokenization.
Token IDs: [15496, 0, 428, 318, 257, 1332, 13, 3644, 13]
Number of tokens: 9
```

This shows:
- How the text is broken into tokens
- The numerical IDs assigned to each token
- How punctuation is handled
- The total number of tokens generated

## Important Notes
- The script shows the complete tokenization pipeline
- It demonstrates how different models handle the same text
- It includes examples of encoding and decoding tokens
- It shows how special characters are processed
- It illustrates the relationship between text and token IDs

## Usage
Run the script to see how text is processed by different tokenizers. This helps understand:
- The basic process of tokenization
- How different models handle text
- The relationship between text and token IDs
- Why tokenization is necessary
- How to work with tokenized text

## Common Questions
1. **Why do we need tokenization?**
   - Computers can only process numbers
   - Tokenization converts text to numbers
   - It helps models understand text structure

2. **Why are there different tokenizers?**
   - Different models have different needs
   - Some are better for specific types of text
   - They use different strategies for breaking down text

3. **How does tokenization affect model performance?**
   - Better tokenization can improve model understanding
   - It affects how models handle unknown words
   - It impacts the model's vocabulary size

## Further Learning Resources

### Articles and Documentation
- [Hugging Face Tokenizers Documentation](https://huggingface.co/docs/tokenizers/index) - Official documentation
- [Understanding Tokenization](https://huggingface.co/learn/nlp-course/chapter6/1) - Step-by-step guide
- [Tokenization Strategies](https://huggingface.co/learn/nlp-course/chapter6/2) - Different approaches

### Videos
- [Introduction to Tokenization](https://www.youtube.com/watch?v=zHvTiHr506c) - Basic concepts
- [Tokenization in Practice](https://www.youtube.com/watch?v=zHvTiHr506c) - Real-world examples
- [Understanding BPE and WordPiece](https://www.youtube.com/watch?v=zHvTiHr506c) - Technical details

### Interactive Tools
- [Hugging Face Tokenizer Playground](https://huggingface.co/tokenizer) - Try it yourself
- [BERT Tokenizer Visualizer](https://bertviz.com/) - Visualize tokenization
- [GPT-2 Tokenizer Explorer](https://gpt2tokenizer.com/) - Explore GPT-2 tokenization

### Books
- "Natural Language Processing with Transformers" by Lewis Tunstall et al.
- "Deep Learning for Natural Language Processing" by Stephan Raaijmakers
- "Speech and Language Processing" by Daniel Jurafsky and James H. Martin 