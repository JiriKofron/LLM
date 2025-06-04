"""
Training Relationships Example

This script demonstrates how training can influence how the model
understands relationships between words.
"""

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def demonstrate_training_influence():
    print("=== How Training Influences Relationships ===\n")
    
    # Load BERT model and tokenizer
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    embedding_layer = model.embeddings.word_embeddings
    
    # 1. Show initial relationships
    print("1. Initial Relationships:")
    word = "bank"
    related_words = {
        "Financial": ["money", "account", "loan", "deposit"],
        "Geographical": ["river", "water", "shore", "stream"]
    }
    
    # Get initial embeddings
    word_id = tokenizer.encode(word, add_special_tokens=False)[0]
    word_emb = embedding_layer.weight[word_id].detach().numpy()
    
    print(f"\n   Initial relationships for '{word}':")
    for category, words in related_words.items():
        print(f"\n   {category} relationships:")
        for related_word in words:
            related_id = tokenizer.encode(related_word, add_special_tokens=False)[0]
            related_emb = embedding_layer.weight[related_id].detach().numpy()
            similarity = cosine_similarity(word_emb.reshape(1, -1), related_emb.reshape(1, -1))[0][0]
            print(f"   - {word} and {related_word}: {similarity:.3f}")
    
    # 2. Show how training would influence this
    print("\n2. How Training Would Influence This:")
    print("   If you want the model to associate 'bank' more with money:")
    print("   - Show it more examples of 'bank' used in financial contexts")
    print("   - The model would learn to adjust the embeddings")
    print("   - 'bank' would become more similar to financial terms")
    print("   - Less similar to geographical terms")
    
    # 3. Demonstrate with a simple example
    print("\n3. Simple Training Example:")
    print("   Before training:")
    print("   - 'bank' might be equally similar to 'money' and 'river'")
    print("   - Similarity to 'money': ~0.5")
    print("   - Similarity to 'river': ~0.5")
    
    print("\n   After training with financial context:")
    print("   - 'bank' would be more similar to 'money'")
    print("   - Similarity to 'money' might increase to ~0.8")
    print("   - Similarity to 'river' might decrease to ~0.3")
    
    # 4. Show how this works in practice
    print("\n4. How This Works in Practice:")
    print("   - The model sees many examples of how words are used")
    print("   - It learns which relationships are more important")
    print("   - It adjusts the embeddings to reflect these relationships")
    print("   - The dimensions capture these learned relationships")
    
    print("\n=== Key Points ===")
    print("1. Training Influence:")
    print("   - You can influence how the model understands relationships")
    print("   - By showing it more examples of certain relationships")
    print("   - The model learns to adjust the embeddings accordingly")
    
    print("\n2. How It Works:")
    print("   - The model sees patterns in how words are used")
    print("   - It learns which relationships are more common")
    print("   - It adjusts the dimensions to capture these relationships")
    print("   - Words become more similar to their common associations")
    
    print("\n3. Practical Applications:")
    print("   - You can train the model for specific domains")
    print("   - You can emphasize certain relationships")
    print("   - You can make the model better at understanding specific contexts")

if __name__ == "__main__":
    demonstrate_training_influence() 