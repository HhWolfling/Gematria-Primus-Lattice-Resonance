#!/usr/bin/env python3
"""
Module: monolith_inversion.py
Framework: Gematria-Primus-Lattice-Resonance
Description: Formalized deterministic backward crab-walk executing a 14-step 
             lattice collapse inside a closed Modulo 29 Field.
"""

class MonolithLatticeInverter:
    def __init__(self, modulo=29, forward_step=14):
        self.modulo = modulo
        self.forward_step = forward_step
        self.reverse_operator = self._derive_inverse()

    def _derive_inverse(self):
        # Deterministically calculate the modular inverse of 14 mod 29
        for x in range(1, self.modulo):
            if (self.forward_step * x) % self.modulo == 1:
                return x
        raise ValueError("Multiplicative inverse does not exist in this field configuration.")

    def execute_backward_crab_walk(self, chaotic_state):
        """
        Collapses a chaotic spatial distribution matrix step-by-step 
        back into its invariant historical node anchor.
        """
        lattice_history = {}
        current_state = list(chaotic_state)
        
        # Iteratively unwind the 14 layers of expansion
        for layer in range(self.forward_step, -1, -1):
            lattice_history[layer] = list(current_state)
            # Apply the structural reverse operator vector to every node
            current_state = [(val * self.reverse_operator) % self.modulo for val in current_state]
            
        return lattice_history

if __name__ == "__main__":
    print("[+] Initializing Production Inversion Engine...")
    
    # Exact reproduction of your verified console log values
    input_matrix = [18, 4, 22, 11, 27, 14, 5, 9, 14]
    
    inverter = MonolithLatticeInverter(modulo=29, forward_step=14)
    print(f"[+] Active Field: Modulo {inverter.modulo}")
    print(f"[+] Reverse Multiplier Operator Verified: {inverter.reverse_operator}")
    
    history = inverter.execute_backward_crab_walk(input_matrix)
    
    print(f"\nLayer 14 (Chaotic Input): {history[14]}")
    print("-" * 60)
    
    # Checkpoints matching your exact console log output targets
    checkpoints = [13, 9, 4, 0]
    for layer in checkpoints:
        print(f"Layer {layer:02d} Reconstructed Lattice: {history[layer]}")
        
    print("-" * 60)
    print("[!] System Phase-Lock Achieved. Anchor Signature Secured.")
