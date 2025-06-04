"""
Embedding Storage Example

This script demonstrates how embeddings are stored in the model
and how they persist between model loads.
"""

from transformers import BertTokenizer, BertModel
import torch
import os

def demonstrate_embedding_storage():
    print("=== How Embeddings are Stored ===\n")
    
    # 1. Show model files
    print("1. Model Files:")
    model_name = 'bert-base-uncased'
    print(f"   When you download '{model_name}', you get these files:")
    print("   - config.json: Model configuration")
    print("   - pytorch_model.bin: All model parameters (including embeddings)")
    print("   - vocab.txt: Vocabulary file")
    
    # 2. Load model and show embedding layer
    print("\n2. Embedding Layer in Model:")
    model = BertModel.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    
    # Get the embedding layer
    embedding_layer = model.embeddings.word_embeddings
    
    print(f"   Embedding matrix shape: {embedding_layer.weight.shape}")
    print(f"   This means: {embedding_layer.weight.shape[0]} tokens × {embedding_layer.weight.shape[1]} dimensions")
    
    # 3. Show how embeddings persist
    print("\n3. Embedding Persistence:")
    print("   - Embeddings are stored in the model file")
    print("   - They persist between model loads")
    print("   - You don't need to retrain the model")
    
    # 4. Demonstrate with a word
    word = "bank"
    token_id = tokenizer.encode(word, add_special_tokens=False)[0]
    
    print(f"\n4. Example for word '{word}':")
    print(f"   Token ID: {token_id}")
    print(f"   This ID maps to a specific row in the embedding matrix")
    print(f"   First 5 dimensions of embedding: {embedding_layer.weight[token_id][:5]}")
    
    # 5. Show how to save and load embeddings
    print("\n5. Saving and Loading:")
    print("   - Model.save_pretrained('path/to/save')")
    print("   - Model.from_pretrained('path/to/save')")
    print("   - Embeddings are automatically saved and loaded")
    
    print("\n=== Key Points ===")
    print("1. Embeddings are stored as a matrix in the model file")
    print("2. Each token ID maps to a specific row in this matrix")
    print("3. The matrix is saved with the model and persists between loads")
    print("4. You don't need to retrain the model each time you use it")
    print("5. The embeddings capture the relationships learned during training")

if __name__ == "__main__":
    demonstrate_embedding_storage() 