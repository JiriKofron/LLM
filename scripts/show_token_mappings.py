"""
Token ID Mapping Demonstrator

This script demonstrates how language models map words to token IDs and vice versa.
It shows the relationship between words and their corresponding IDs in the model's vocabulary.

Key Concepts:
- Token IDs: Unique numerical identifiers assigned to words/subwords in the model's vocabulary
- Vocabulary: The set of all known tokens (words and subwords) that the model can understand
- Tokenization: The process of converting text into token IDs that the model can process

Example Usage:
    python show_token_mappings.py
"""

from transformers import GPT2Tokenizer, BertTokenizer

def show_gpt2_mappings():
    """
    Demonstrates token ID mappings using GPT-2's tokenizer.
    Shows how words are converted to IDs and back.
    """
    # Initialize GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    
    # Example words of different types
    words = [
        "hello",           # Simple word
        "world",           # Simple word
        "artificial",      # Longer word
        "intelligence",    # Longer word
        "transformer",     # Technical term
        "neural",          # Technical term
    ]
    
    print("\n=== GPT-2 Token ID Mappings ===\n")
    
    for word in words:
        # Get all token IDs for the word
        token_ids = tokenizer.encode(word, add_special_tokens=False)
        tokens = tokenizer.tokenize(word)
        
        print(f"Word: {word}")
        print(f"Tokens: {tokens}")
        print(f"Token IDs: {token_ids}")
        print(f"Converting IDs back to word: {tokenizer.decode(token_ids)}")
        print()

def show_bert_mappings():
    """
    Demonstrates token ID mappings using BERT's tokenizer.
    Shows how words are converted to IDs and back.
    """
    # Initialize BERT tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Example words of different types
    words = [
        "hello",           # Simple word
        "world",           # Simple word
        "artificial",      # Longer word
        "intelligence",    # Longer word
        "transformer",     # Technical term
        "neural",          # Technical term
    ]
    
    print("\n=== BERT Token ID Mappings ===\n")
    
    for word in words:
        # Get all token IDs for the word
        token_ids = tokenizer.encode(word, add_special_tokens=False)
        tokens = tokenizer.tokenize(word)
        
        print(f"Word: {word}")
        print(f"Tokens: {tokens}")
        print(f"Token IDs: {token_ids}")
        print(f"Converting IDs back to word: {tokenizer.decode(token_ids)}")
        print()

def show_vocabulary_stats():
    """
    Shows statistics about the vocabulary size of both tokenizers.
    """
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    print("\n=== Vocabulary Statistics ===\n")
    print(f"GPT-2 vocabulary size: {len(gpt2_tokenizer)}")
    print(f"BERT vocabulary size: {len(bert_tokenizer)}")
    print("\nNote: These numbers represent the total number of unique tokens")
    print("(words and subwords) that each model can understand.")

def demonstrate_subword_tokenization():
    """
    Demonstrates how BERT and GPT-2 handle subword tokenization differently,
    and how this can affect model behavior.
    """
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    word = "transformer"
    
    print("\n=== Subword Tokenization Analysis ===\n")
    print(f"Word: {word}")
    
    # GPT-2 tokenization
    gpt2_tokens = gpt2_tokenizer.tokenize(word)
    gpt2_ids = gpt2_tokenizer.encode(word, add_special_tokens=False)
    
    print("\nGPT-2 Tokenization:")
    print(f"Tokens: {gpt2_tokens}")
    print(f"Token IDs: {gpt2_ids}")
    print(f"Decoded back: {gpt2_tokenizer.decode(gpt2_ids)}")
    
    # BERT tokenization
    bert_tokens = bert_tokenizer.tokenize(word)
    bert_ids = bert_tokenizer.encode(word, add_special_tokens=False)
    
    print("\nBERT Tokenization:")
    print(f"Tokens: {bert_tokens}")
    print(f"Token IDs: {bert_ids}")
    print(f"Decoded back: {bert_tokenizer.decode(bert_ids)}")
    
    print("\nPotential Issues:")
    print("1. Different tokenization can lead to different model interpretations")
    print("2. Subword tokens (marked with ##) need to be handled carefully")
    print("3. Models might process the same word differently")
    print("4. This can affect model performance on specific tasks")

def main():
    """
    Main function to run all demonstrations.
    """
    print("Token ID Mapping Demonstrator")
    print("============================")
    print("\nThis script shows how language models map words to token IDs")
    print("and how these mappings are consistent and reversible.\n")
    
    show_gpt2_mappings()
    show_bert_mappings()
    show_vocabulary_stats()
    demonstrate_subword_tokenization()

if __name__ == "__main__":
    main() 