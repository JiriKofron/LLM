"""
Embedding Dimensions Example

This script demonstrates what embedding dimensions are and how they work
with a simplified example of 3-dimensional embeddings.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_dimensions():
    print("=== Understanding Embedding Dimensions ===\n")
    
    # 1. Simple 3D example
    print("1. Simple 3D Example:")
    print("   Imagine we have 3 dimensions:")
    print("   - Dimension 1: Concreteness (how physical/tangible)")
    print("   - Dimension 2: Emotionality (how emotional)")
    print("   - Dimension 3: Formality (how formal)")
    
    # Example words with their hypothetical 3D embeddings
    words_3d = {
        "rock": [0.9, 0.1, 0.3],    # Very concrete, not emotional, somewhat formal
        "love": [0.2, 0.9, 0.4],    # Not concrete, very emotional, somewhat formal
        "the": [0.1, 0.1, 0.8],     # Not concrete, not emotional, very formal
        "ouch": [0.3, 0.8, 0.1]     # Somewhat concrete, very emotional, informal
    }
    
    print("\n2. Example 3D Embeddings:")
    for word, embedding in words_3d.items():
        print(f"   {word}: {embedding}")
    
    # 2. Real BERT embeddings
    print("\n3. Real BERT Embeddings:")
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Get embedding layer
    embedding_layer = model.embeddings.word_embeddings
    
    print(f"   BERT uses {embedding_layer.weight.shape[1]} dimensions")
    print("   Each dimension captures some aspect of meaning")
    
    # 3. Show how dimensions capture relationships
    print("\n4. How Dimensions Capture Relationships:")
    print("   - Similar words have similar values in similar dimensions")
    print("   - Different words have different patterns across dimensions")
    print("   - The model learns which dimensions are important for which relationships")
    
    # 4. Demonstrate with real words
    words = ["king", "queen", "man", "woman"]
    print(f"\n5. Real Example with {len(words)} words:")
    
    for word in words:
        token_id = tokenizer.encode(word, add_special_tokens=False)[0]
        embedding = embedding_layer.weight[token_id]
        print(f"   {word}:")
        print(f"   - First 5 dimensions: {embedding[:5].numpy()}")
        print(f"   - Total dimensions: {len(embedding)}")
    
    print("\n=== Key Points ===")
    print("1. Each dimension captures some aspect of meaning")
    print("2. More dimensions = more aspects can be captured")
    print("3. Similar words have similar patterns across dimensions")
    print("4. The model learns which dimensions are important")
    print("5. BERT uses 768 dimensions to capture many subtle aspects of meaning")

if __name__ == "__main__":
    demonstrate_dimensions() 