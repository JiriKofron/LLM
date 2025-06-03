from transformers import GPT2Tokenizer, BertTokenizer

def demonstrate_tokenization():
    # Example text
    text = "Hello! This is a test of tokenization. Let's see how it works."
    
    # 1. GPT-2 Tokenizer (subword tokenization)
    print("=== GPT-2 Tokenization ===")
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    gpt2_tokens = gpt2_tokenizer.encode(text)
    print(f"Original text: {text}")
    print(f"Token IDs: {gpt2_tokens}")
    print(f"Decoded tokens: {gpt2_tokenizer.decode(gpt2_tokens)}")
    print(f"Number of tokens: {len(gpt2_tokens)}")
    
    # 2. BERT Tokenizer (another type of subword tokenization)
    print("\n=== BERT Tokenization ===")
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    bert_tokens = bert_tokenizer.encode(text)
    print(f"Original text: {text}")
    print(f"Token IDs: {bert_tokens}")
    print(f"Decoded tokens: {bert_tokenizer.decode(bert_tokens)}")
    print(f"Number of tokens: {len(bert_tokens)}")
    
    # 3. Let's look at how different tokenizers handle the same word
    word = "stonehenge"
    print(f"\n=== Tokenizing the word '{word}' ===")
    print(f"GPT-2 tokens: {gpt2_tokenizer.tokenize(word)}")
    print(f"BERT tokens: {bert_tokenizer.tokenize(word)}")

if __name__ == "__main__":
    demonstrate_tokenization() 