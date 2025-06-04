"""
Embeddings Example

This script demonstrates the difference between static and contextual embeddings.
It shows how the same word can have different representations based on context.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np

def demonstrate_embeddings():
    # Initialize BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    # Example sentences with the word "bank" in different contexts
    sentences = [
        "I went to the bank to deposit money",  # Financial context
        "I sat by the bank of the river",       # River context
    ]
    
    print("=== Embeddings Demonstration ===\n")
    
    for sentence in sentences:
        print(f"\nSentence: {sentence}")
        
        # Tokenize the sentence
        tokens = tokenizer.tokenize(sentence)
        print(f"Tokens: {tokens}")
        
        # Get the position of "bank" in the tokens
        bank_index = tokens.index("bank")
        
        # Get embeddings
        inputs = tokenizer(sentence, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        
        # Get the embedding for "bank"
        bank_embedding = outputs.last_hidden_state[0][bank_index + 1]  # +1 for [CLS] token
        
        # Print a small part of the embedding to show it's different
        print(f"Embedding for 'bank' (first 5 dimensions): {bank_embedding[:5].numpy()}")
    
    print("\n=== Key Points ===")
    print("1. Each word is represented as a vector of numbers")
    print("2. In contextual embeddings (like BERT):")
    print("   - The same word can have different embeddings in different contexts")
    print("   - This helps the model understand the meaning better")
    print("3. In static embeddings (like Word2Vec):")
    print("   - The same word always has the same embedding")
    print("   - This is simpler but less flexible")

if __name__ == "__main__":
    demonstrate_embeddings() 