"""
Pattern Relationships Example

This script demonstrates how patterns in dimensions show relationships
between words and how these patterns emerge from context.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_patterns():
    print("=== Understanding Pattern Relationships ===\n")
    
    # Load BERT model and tokenizer
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    embedding_layer = model.embeddings.word_embeddings
    
    # 1. Show relationship patterns
    print("1. Relationship Patterns:")
    relationship_groups = {
        "Gender Pairs": [
            ("king", "queen"),
            ("man", "woman"),
            ("boy", "girl"),
            ("actor", "actress")
        ],
        "Size Pairs": [
            ("big", "small"),
            ("huge", "tiny"),
            ("large", "little"),
            ("giant", "dwarf")
        ],
        "Emotion Pairs": [
            ("happy", "sad"),
            ("joy", "sorrow"),
            ("love", "hate"),
            ("smile", "frown")
        ]
    }
    
    # 2. Show similarities within relationship groups
    print("\n2. Similarities in Relationship Groups:")
    for group_name, pairs in relationship_groups.items():
        print(f"\n   {group_name}:")
        for word1, word2 in pairs:
            # Get embeddings
            id1 = tokenizer.encode(word1, add_special_tokens=False)[0]
            id2 = tokenizer.encode(word2, add_special_tokens=False)[0]
            emb1 = embedding_layer.weight[id1].detach().numpy()
            emb2 = embedding_layer.weight[id2].detach().numpy()
            
            # Calculate similarity
            similarity = cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1))[0][0]
            
            print(f"   - {word1} and {word2}: {similarity:.3f}")
            
            # Show first 5 dimensions where they're similar
            print(f"     First 5 dimensions where they're similar:")
            for i in range(5):
                print(f"     Dimension {i}: {word1}={emb1[i]:.3f}, {word2}={emb2[i]:.3f}")
    
    # 3. Show how context affects relationships
    print("\n3. How Context Affects Relationships:")
    context_examples = [
        ("bank", "river"),    # Financial vs geographical context
        ("bank", "money"),    # Financial context
        ("bank", "water"),    # Geographical context
    ]
    
    print("\n   Context Examples:")
    for word1, word2 in context_examples:
        id1 = tokenizer.encode(word1, add_special_tokens=False)[0]
        id2 = tokenizer.encode(word2, add_special_tokens=False)[0]
        emb1 = embedding_layer.weight[id1].detach().numpy()
        emb2 = embedding_layer.weight[id2].detach().numpy()
        
        similarity = cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1))[0][0]
        print(f"   - {word1} and {word2}: {similarity:.3f}")
    
    print("\n=== Key Points ===")
    print("1. Pattern Recognition:")
    print("   - Similar words have similar patterns in their dimensions")
    print("   - These patterns emerge from how words are used together")
    print("   - The model learns these patterns during training")
    
    print("\n2. Context Matters:")
    print("   - Words can have different relationships in different contexts")
    print("   - The same word can have different patterns in different uses")
    print("   - The model learns to capture these contextual relationships")
    
    print("\n3. Relationship Types:")
    print("   - Some dimensions capture gender relationships")
    print("   - Others capture size relationships")
    print("   - Others capture emotional relationships")
    print("   - The model learns to use dimensions to capture these relationships")

if __name__ == "__main__":
    demonstrate_patterns() 