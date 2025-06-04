from transformers import GPT2Tokenizer, BertTokenizer

def analyze_word_breakdown():
    # Words that might be unknown to the model
    words = [
        "stonehenge",  # Compound word
        "cyberpunk",   # Modern term
        "blockchain",  # Technical term
        "quantumcomputing",  # Scientific term
        "xyzzy",      # Completely made up word
        "flibbertigibbet",  # Rare English word
        "supercalifragilisticexpialidocious"  # Long made-up word
    ]
    
    # Initialize tokenizers
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    print("=== How Different Tokenizers Break Down Unknown Words ===\n")
    
    for word in words:
        print(f"\nWord: {word}")
        print(f"GPT-2 breakdown: {gpt2_tokenizer.tokenize(word)}")
        print(f"BERT breakdown: {bert_tokenizer.tokenize(word)}")
        
        # Show how the model might understand these words
        print("\nPossible understanding based on subwords:")
        bert_tokens = bert_tokenizer.tokenize(word)
        for token in bert_tokens:
            if token.startswith('##'):
                print(f"- {token[2:]} is a continuation of the previous token")
            elif token == "[UNK]":
                print(f"- [UNK] means the tokenizer has no idea what this is")
            else:
                print(f"- {token} is a known word or prefix")
        
        # Try to encode the word to see if it uses [UNK]
        try:
            gpt2_ids = gpt2_tokenizer.encode(word)
            bert_ids = bert_tokenizer.encode(word)
            print(f"\nToken IDs:")
            print(f"GPT-2 IDs: {gpt2_ids}")
            print(f"BERT IDs: {bert_ids}")
        except Exception as e:
            print(f"Error encoding word: {e}")

if __name__ == "__main__":
    analyze_word_breakdown() 