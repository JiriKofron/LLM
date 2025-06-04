"""
Token and Embedding Relationship

This script demonstrates how tokens, vocabulary, and embeddings are related.
It shows how token IDs map to embeddings in a language model.
"""

from transformers import BertTokenizer, BertModel
import torch

def demonstrate_relationship():
    # Initialize BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    # Example word
    word = "bank"
    
    print("=== Token, Vocabulary, and Embedding Relationship ===\n")
    
    # 1. Show tokenization
    tokens = tokenizer.tokenize(word)
    print(f"1. Tokenization:")
    print(f"   Word '{word}' is tokenized as: {tokens}")
    
    # 2. Show vocabulary mapping
    token_ids = tokenizer.encode(word, add_special_tokens=False)
    print(f"\n2. Vocabulary Mapping:")
    print(f"   Token IDs in vocabulary: {token_ids}")
    print(f"   Total vocabulary size: {len(tokenizer)}")
    
    # 3. Show embedding mapping
    print(f"\n3. Embedding Mapping:")
    print(f"   Each token ID maps to an embedding vector")
    print(f"   Embedding dimension: {model.config.hidden_size}")
    
    # 4. Get and show actual embeddings
    inputs = tokenizer(word, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get embeddings for the word
    word_embeddings = outputs.last_hidden_state[0][1:-1]  # Remove [CLS] and [SEP]
    
    print(f"\n4. Actual Embeddings:")
    print(f"   First 5 dimensions of embedding for '{word}':")
    print(f"   {word_embeddings[0][:5].numpy()}")
    
    print("\n=== Key Points ===")
    print("1. Vocabulary:")
    print("   - Contains all known tokens")
    print("   - Maps tokens to unique IDs")
    print("   - Fixed size (e.g., 30,000 for BERT)")
    
    print("\n2. Tokens:")
    print("   - Are the basic units of text")
    print("   - Have unique IDs in vocabulary")
    print("   - Can be words or subwords")
    
    print("\n3. Embeddings:")
    print("   - Are the actual numerical representations")
    print("   - Each token ID maps to an embedding")
    print("   - Learned during model training")
    print("   - Capture meaning and relationships")

if __name__ == "__main__":
    demonstrate_relationship() 