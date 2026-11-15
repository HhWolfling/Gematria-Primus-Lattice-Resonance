# logic/cicada_twin_overlay.py
"""
[THREAD-CHARLIE // CICADA_ANOMALY]
Cicada 2014 Dual Order 5 Companion Matrix Collision Engine
Layers the twin 'interconnected.mp3' squares to extract differential Vigenere shift offsets.
"""

import numpy as np

class CicadaTwinOverlay:
    def __init__(self):
        # Twin 1: The perfect palindrome matrix you provided
        self.twin_1 = np.array([
            [272, 138, 341, 131, 151],
            [366, 199, 130, 320,  18],
            [226, 245,  91, 245, 226],
            [ 18, 320, 130, 199, 366],
            [151, 131, 341, 138, 272]
        ])
        
        # Twin 2: The second companion Order 5 square hidden in the MP3 text payload
        # This twin also sums perfectly to 1033 but shifts its internal vector distributions
        self.twin_2 = np.array([
            [272, 320, 130, 138, 173],
            [131, 199, 341, 181, 181],
            [366, 131,  91, 219, 226],
            [113, 245, 130, 199, 346],
            [151, 138, 341, 296, 107]
        ])
        
        self.modulo_field = 29

    def collide_matrices(self):
        print("🌀 EXECUTING COMPANION MATRIX COLLISION")
        print("═" * 55)
        
        # Calculate raw spatial differential map
        differential_matrix = self.twin_1 - self.twin_2
        
        print("Raw Spatial Differential Vector Map (Twin 1 - Twin 2):")
        for row in differential_matrix:
            print(f"  [ " + "  ".join(f"{num:4d}" for num in row) + " ]")
            
        print("\n🔮 FLATTENING DIFFERENTIALS ONTO MODULO 29 RUNIC RING")
        print("─" * 55)
        
        # Squeeze the shifts into valid Gematria shift indices (0 to 28)
        runic_shifts = differential_matrix % self.modulo_field
        
        print("Runic Cipher-Shift Matrix (Vigenère Offset Map):")
        for row in runic_shifts:
            print(f"  [ " + "  ".join(f"{num:2d}" for num in row) + " ]")
            
        print("═" * 55)
        print("🧬 Wave-front collapsed. Shifts ready for Liber Primus decryption loops.")

if __name__ == "__main__":
    overlay = CicadaTwinOverlay()
    overlay.collide_matrices()
