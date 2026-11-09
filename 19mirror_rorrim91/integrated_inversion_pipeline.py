#!/usr/bin/env python3
"""
Integrated Inversion Pipeline with Raw Document Parsing
Ingests 'source_text.txt' and processes lines via the Reverse 14-Step Operator.
"""
import os

def load_and_sieve_source():
    FIELD_MODULO = 29
    REVERSE_OPERATOR = 25  # Derived inverse of 14 mod 29
    filename = "source_text.txt"
    
    if not os.path.exists(filename):
        # Fallback with dummy data if file is missing to ensure script execution
        print(f"[-] {filename} not found. Creating a default mock stream for simulation.")
        with open(filename, "w") as f:
            f.write("LATTICE RESONANCE TEST MATRIX BLOCKS")

    print(f"[+] Reading from {filename}...")
    with open(filename, "r", encoding="utf-8") as f:
        raw_text = f.read().upper()

    # Convert text to Futhark-compatible Modulo 29 indices (Simple tokenization example)
    # Filter out characters to simulate character mass extraction
    token_stream = [ord(char) % FIELD_MODULO for char in raw_text if char.isalnum()]
    print(f"[+] Extracted {len(token_stream)} typographical tokens.")
    
    # Process the stream in blocks (simulating the monolith grid layout)
    block_size = 8
    processed_blocks = []
    
    for i in range(0, len(token_stream), block_size):
        block = token_stream[i:i+block_size]
        if len(block) < block_size:
            block += [0] * (block_size - len(block)) # Padding to maintain grid dimensions
            
        # Execute the 14-step collapse on the active block
        current_state = list(block)
        for _ in range(14):
            current_state = [(val * REVERSE_OPERATOR) % FIELD_MODULO for val in current_state]
        
        processed_blocks.append(current_state)
        
    print(f"[=>] Inversion complete. First 3 collapsed blocks: {processed_blocks[:3]}")
    return processed_blocks

if __name__ == "__main__":
    load_and_sieve_source()
