"""
Byte-Pair Encoding (BPE) Example

This script demonstrates how BPE works with a simple example.
It shows the step-by-step process of how BPE builds its vocabulary.
"""

def demonstrate_bpe_process():
    # Simple example text
    text = "low lower lowest"
    
    print("=== BPE Process Demonstration ===\n")
    print(f"Original text: {text}")
    
    # Step 1: Start with individual characters
    print("\nStep 1: Individual characters")
    chars = list(text)
    print(f"Characters: {chars}")
    
    # Step 2: Count character pairs
    print("\nStep 2: Common character pairs")
    pairs = []
    for i in range(len(chars)-1):
        pairs.append(chars[i] + chars[i+1])
    
    # Count pair frequencies
    pair_counts = {}
    for pair in pairs:
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 1
    
    print("Pair frequencies:")
    for pair, count in pair_counts.items():
        print(f"  {pair}: {count}")
    
    # Step 3: Merge most common pair
    print("\nStep 3: Merge most common pair")
    most_common_pair = max(pair_counts.items(), key=lambda x: x[1])[0]
    print(f"Most common pair: {most_common_pair}")
    
    # Step 4: Show how this would be used in tokenization
    print("\nStep 4: How this affects tokenization")
    print("In a real BPE implementation:")
    print("1. This process would be repeated many times")
    print("2. The most common pairs would become part of the vocabulary")
    print("3. Each token would get a unique ID")
    print("\nFor example, 'low' might be tokenized as:")
    print("  'l' + 'ow' (if 'ow' was a common pair)")
    print("  Or 'low' (if it was common enough to be a single token)")
    
    print("\nNote: This is a simplified example. Real BPE implementations:")
    print("- Work with much larger datasets")
    print("- Build a vocabulary of thousands of tokens")
    print("- Use more sophisticated merging strategies")
    print("- Handle special cases and edge conditions")

if __name__ == "__main__":
    demonstrate_bpe_process() 