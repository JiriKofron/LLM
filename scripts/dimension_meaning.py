"""
Dimension Meaning Example

This script demonstrates how dimensions work together to capture meaning,
rather than having predefined meanings themselves.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_dimension_meaning():
    print("=== How Dimensions Actually Work ===\n")
    
    # Load BERT model and tokenizer
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Get embedding layer
    embedding_layer = model.embeddings.word_embeddings
    
    # 1. Show that dimensions don't have predefined meanings
    print("1. Dimensions Don't Have Predefined Meanings:")
    print("   - Each dimension is just a number")
    print("   - The model learns what these numbers mean")
    print("   - We don't know exactly what each dimension represents")
    print("   - Meaning emerges from how dimensions work together")
    
    # 2. Demonstrate with similar words
    word_pairs = [
        ("king", "queen"),
        ("man", "woman"),
        ("happy", "sad"),
        ("big", "small")
    ]
    
    print("\n2. How Similar Words Have Similar Patterns:")
    for word1, word2 in word_pairs:
        # Get embeddings
        id1 = tokenizer.encode(word1, add_special_tokens=False)[0]
        id2 = tokenizer.encode(word2, add_special_tokens=False)[0]
        emb1 = embedding_layer.weight[id1]
        emb2 = embedding_layer.weight[id2]
        
        # Calculate similarity (using detach() to fix the error)
        similarity = cosine_similarity(
            emb1.detach().numpy().reshape(1, -1), 
            emb2.detach().numpy().reshape(1, -1)
        )[0][0]
        
        print(f"\n   {word1} and {word2}:")
        print(f"   - Similarity: {similarity:.3f}")
        print(f"   - First 5 dimensions of {word1}: {emb1.detach().numpy()[:5]}")
        print(f"   - First 5 dimensions of {word2}: {emb2.detach().numpy()[:5]}")
    
    # 3. Show how dimensions work together
    print("\n3. How Dimensions Work Together:")
    print("   - No single dimension captures a complete concept")
    print("   - Meaning comes from patterns across many dimensions")
    print("   - Similar words have similar patterns")
    print("   - Different words have different patterns")
    
    # 4. Demonstrate with a specific example
    word = "king"
    token_id = tokenizer.encode(word, add_special_tokens=False)[0]
    embedding = embedding_layer.weight[token_id]
    
    print(f"\n4. Example with word '{word}':")
    print("   - No single dimension means 'royalty'")
    print("   - The pattern across all 768 dimensions captures the meaning")
    print("   - First 10 dimensions:")
    for i, val in enumerate(embedding.detach().numpy()[:10]):
        print(f"   Dimension {i}: {val:.3f}")
    
    print("\n=== Key Points ===")
    print("1. Dimensions don't have predefined meanings")
    print("2. The model learns what each dimension represents")
    print("3. Meaning emerges from patterns across dimensions")
    print("4. Similar words have similar patterns")
    print("5. No single dimension captures a complete concept")

if __name__ == "__main__":
    demonstrate_dimension_meaning() 