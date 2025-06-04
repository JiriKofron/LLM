"""
Training and Embeddings Example

This script demonstrates how training affects word embeddings
and how the model learns to represent relationships between words.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_training_effects():
    # Initialize BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    # Example word pairs to show relationships
    word_pairs = [
        ("king", "queen"),      # Royalty relationship
        ("man", "woman"),       # Gender relationship
        ("happy", "sad"),       # Opposite emotions
        ("big", "small"),       # Opposite sizes
    ]
    
    print("=== How Training Affects Embeddings ===\n")
    
    for word1, word2 in word_pairs:
        # Get embeddings for both words
        inputs1 = tokenizer(word1, return_tensors="pt")
        inputs2 = tokenizer(word2, return_tensors="pt")
        
        with torch.no_grad():
            outputs1 = model(**inputs1)
            outputs2 = model(**inputs2)
        
        # Get the embeddings (remove [CLS] and [SEP])
        emb1 = outputs1.last_hidden_state[0][1:-1]
        emb2 = outputs2.last_hidden_state[0][1:-1]
        
        # Calculate similarity
        similarity = cosine_similarity(emb1.numpy(), emb2.numpy())[0][0]
        
        print(f"Words: {word1} and {word2}")
        print(f"Similarity: {similarity:.3f}")
        print(f"First 5 dimensions of {word1}: {emb1[0][:5].numpy()}")
        print(f"First 5 dimensions of {word2}: {emb2[0][:5].numpy()}")
        print()
    
    print("=== How Training Works ===")
    print("1. Initial State:")
    print("   - Words start with random embeddings")
    print("   - No meaningful relationships")
    
    print("\n2. During Training:")
    print("   - Model sees many examples of word usage")
    print("   - Learns which words appear in similar contexts")
    print("   - Adjusts embeddings to capture relationships")
    
    print("\n3. After Training:")
    print("   - Similar words have similar embeddings")
    print("   - Relationships are captured in the numbers")
    print("   - Model can understand word meanings and relationships")
    
    print("\n4. What the Model Learns:")
    print("   - Semantic relationships (king-queen)")
    print("   - Syntactic relationships (verb forms)")
    print("   - Contextual relationships (word meanings)")
    print("   - Domain-specific relationships (technical terms)")

if __name__ == "__main__":
    demonstrate_training_effects() 