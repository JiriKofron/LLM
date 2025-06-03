from transformers import GPT2Tokenizer, BertTokenizer

def explain_token_ids():
    # Initialize tokenizers
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Example sentences of increasing complexity
    examples = [
        "Hello world",  # Simple
        "The quick brown fox",  # Common words
        "Artificial intelligence is fascinating",  # Technical terms
        "The quantum computer processed the data"  # Complex terms
    ]
    
    print("=== Understanding Token IDs ===\n")
    
    for example in examples:
        print(f"\nExample: '{example}'")
        
        # GPT-2 Tokenization
        print("\nGPT-2 Tokenization:")
        gpt2_tokens = gpt2_tokenizer.tokenize(example)
        gpt2_ids = gpt2_tokenizer.encode(example)
        
        print("Token to ID mapping:")
        for token, token_id in zip(gpt2_tokens, gpt2_ids[1:-1]):  # Skip special tokens
            print(f"'{token}' → {token_id}")
        
        # BERT Tokenization
        print("\nBERT Tokenization:")
        bert_tokens = bert_tokenizer.tokenize(example)
        bert_ids = bert_tokenizer.encode(example)
        
        print("Token to ID mapping:")
        for token, token_id in zip(bert_tokens, bert_ids[1:-1]):  # Skip special tokens
            print(f"'{token}' → {token_id}")
        
        # Explain what these IDs mean
        print("\nWhat these IDs mean:")
        print("1. Each ID is a unique number assigned to a token in the model's vocabulary")
        print("2. The same word will always get the same ID in the same model")
        print("3. Different models (GPT-2 vs BERT) use different ID systems")
        print("4. These IDs are what the model actually processes - not the words themselves")
        
        # Show vocabulary size
        print(f"\nVocabulary size:")
        print(f"GPT-2 vocabulary size: {len(gpt2_tokenizer)}")
        print(f"BERT vocabulary size: {len(bert_tokenizer)}")

if __name__ == "__main__":
    explain_token_ids() 