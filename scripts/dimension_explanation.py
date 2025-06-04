"""
Dimension Explanation Example

This script demonstrates how dimensions work with a simple example
that shows how words can be similar in different ways.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def explain_dimensions():
    print("=== Understanding Dimensions with Simple Examples ===\n")
    
    # 1. Start with a simple example
    print("1. Simple Example:")
    print("   Let's look at how words can be similar in different ways:")
    
    # Example word groups
    word_groups = {
        "Size": ["big", "huge", "large", "small", "tiny"],
        "Emotion": ["happy", "joyful", "sad", "angry", "calm"],
        "Animals": ["dog", "cat", "lion", "tiger", "elephant"],
        "Colors": ["red", "blue", "green", "yellow", "purple"]
    }
    
    # Load BERT model and tokenizer
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    embedding_layer = model.embeddings.word_embeddings
    
    # 2. Show similarities within groups
    print("\n2. Similarities Within Groups:")
    for group_name, words in word_groups.items():
        print(f"\n   {group_name} group:")
        # Compare first word with others
        base_word = words[0]
        base_id = tokenizer.encode(base_word, add_special_tokens=False)[0]
        base_emb = embedding_layer.weight[base_id].detach().numpy()
        
        for word in words[1:]:
            word_id = tokenizer.encode(word, add_special_tokens=False)[0]
            word_emb = embedding_layer.weight[word_id].detach().numpy()
            similarity = cosine_similarity(base_emb.reshape(1, -1), word_emb.reshape(1, -1))[0][0]
            print(f"   - {base_word} and {word}: {similarity:.3f}")
    
    # 3. Show similarities across groups
    print("\n3. Similarities Across Groups:")
    print("   Let's compare words from different groups:")
    
    cross_group_pairs = [
        ("big", "happy"),    # Size vs Emotion
        ("dog", "red"),      # Animal vs Color
        ("happy", "dog"),    # Emotion vs Animal
        ("big", "red")       # Size vs Color
    ]
    
    for word1, word2 in cross_group_pairs:
        id1 = tokenizer.encode(word1, add_special_tokens=False)[0]
        id2 = tokenizer.encode(word2, add_special_tokens=False)[0]
        emb1 = embedding_layer.weight[id1].detach().numpy()
        emb2 = embedding_layer.weight[id2].detach().numpy()
        similarity = cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1))[0][0]
        print(f"   - {word1} and {word2}: {similarity:.3f}")
    
    print("\n=== How Dimensions Actually Work ===")
    print("1. Each dimension is like a feature detector:")
    print("   - Some dimensions might detect size-related features")
    print("   - Others might detect emotion-related features")
    print("   - The model learns these features during training")
    
    print("\n2. Words are similar when they share features:")
    print("   - 'big' and 'huge' are similar because they share size features")
    print("   - 'happy' and 'joyful' are similar because they share emotion features")
    print("   - 'dog' and 'cat' are similar because they share animal features")
    
    print("\n3. The model learns these features automatically:")
    print("   - We don't tell it what each dimension means")
    print("   - It learns to detect useful features")
    print("   - Similar words end up with similar patterns")
    
    print("\n4. It's like learning a language:")
    print("   - When you learn a language, you learn patterns")
    print("   - You don't learn explicit rules for every word")
    print("   - The model does something similar with dimensions")

if __name__ == "__main__":
    explain_dimensions() 