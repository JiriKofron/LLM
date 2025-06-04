from transformers import GPT2Tokenizer, BertTokenizer

def demonstrate_tokenization_process():
    # Initialize tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    
    # Example word that might be split into subwords
    word = "unhappiness"
    
    print(f"\n=== Tokenization Process for '{word}' ===\n")
    
    # Get the tokens
    tokens = tokenizer.tokenize(word)
    token_ids = tokenizer.encode(word)
    
    print(f"Original word: {word}")
    print(f"Split into tokens: {tokens}")
    print(f"Token IDs: {token_ids}")
    
    # Show how the model learned to break down the word
    print("\nHow the model learned to break this down:")
    for token in tokens:
        print(f"Token: {token} -> ID: {tokenizer.convert_tokens_to_ids(token)}")

def compare_tokenization_approaches():
    # Initialize tokenizers
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # Example texts of different types
    examples = [
        "The quick brown fox jumps over the lazy dog",  # Common words
        "The quantum computer processed the data efficiently",  # Technical terms
        "The neural network architecture uses attention mechanisms",  # AI terms
        "The blockchain technology revolutionized cryptocurrency",  # Modern terms
    ]
    
    print("=== Comparing BERT and GPT-2 Tokenization ===\n")
    
    for example in examples:
        print(f"\nText: {example}")
        
        # GPT-2 Tokenization
        gpt2_tokens = gpt2_tokenizer.tokenize(example)
        gpt2_ids = gpt2_tokenizer.encode(example)
        
        print("\nGPT-2 Tokenization:")
        print(f"Tokens: {gpt2_tokens}")
        print(f"Number of tokens: {len(gpt2_tokens)}")
        print(f"Token IDs: {gpt2_ids}")
        
        # BERT Tokenization
        bert_tokens = bert_tokenizer.tokenize(example)
        bert_ids = bert_tokenizer.encode(example)
        
        print("\nBERT Tokenization:")
        print(f"Tokens: {bert_tokens}")
        print(f"Number of tokens: {len(bert_tokens)}")
        print(f"Token IDs: {bert_ids}")
        
        # Analysis
        print("\nAnalysis:")
        print(f"GPT-2 uses {len(gpt2_tokens)} tokens")
        print(f"BERT uses {len(bert_tokens)} tokens")
        print(f"Difference: {len(gpt2_tokens) - len(bert_tokens)} tokens")
        
        # Show how they handle subwords
        print("\nSubword handling:")
        print("GPT-2 subwords:", [t for t in gpt2_tokens if '##' not in t])
        print("BERT subwords:", [t for t in bert_tokens if '##' not in t])

if __name__ == "__main__":
    demonstrate_tokenization_process()
    print("\n" + "="*50 + "\n")
    compare_tokenization_approaches() 