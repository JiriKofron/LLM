"""
Embedding Values Example

This script demonstrates the range and distribution of values
in embedding dimensions.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
import matplotlib.pyplot as plt

def demonstrate_embedding_values():
    print("=== Understanding Embedding Values ===\n")
    
    # Load BERT model and tokenizer
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Get embedding layer
    embedding_layer = model.embeddings.word_embeddings
    
    # Get embeddings for some example words
    words = ["king", "queen", "man", "woman", "happy", "sad"]
    
    print("1. Value Ranges for Example Words:")
    for word in words:
        token_id = tokenizer.encode(word, add_special_tokens=False)[0]
        embedding = embedding_layer.weight[token_id]
        
        # Calculate statistics
        min_val = embedding.min().item()
        max_val = embedding.max().item()
        mean_val = embedding.mean().item()
        std_val = embedding.std().item()
        
        print(f"\n   {word}:")
        print(f"   - Minimum value: {min_val:.3f}")
        print(f"   - Maximum value: {max_val:.3f}")
        print(f"   - Mean value: {mean_val:.3f}")
        print(f"   - Standard deviation: {std_val:.3f}")
    
    # 2. Show distribution of values
    print("\n2. Value Distribution:")
    print("   - Values are not strictly bounded to [-1, 1]")
    print("   - They follow a normal distribution (bell curve)")
    print("   - Most values are close to 0")
    print("   - Some values can be larger or smaller")
    
    # 3. Demonstrate with a specific word
    word = "king"
    token_id = tokenizer.encode(word, add_special_tokens=False)[0]
    embedding = embedding_layer.weight[token_id]
    
    print(f"\n3. Example for word '{word}':")
    print("   First 10 dimensions and their values:")
    for i, val in enumerate(embedding[:10]):
        print(f"   Dimension {i}: {val.item():.3f}")
    
    print("\n=== Key Points ===")
    print("1. Embedding values are not strictly bounded")
    print("2. They typically follow a normal distribution")
    print("3. Most values are close to 0")
    print("4. The exact values don't matter as much as their relative relationships")
    print("5. The model learns to use these values to capture meaning")

if __name__ == "__main__":
    demonstrate_embedding_values() 