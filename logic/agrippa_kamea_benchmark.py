# logic/agrippa_kamea_benchmark.py
"""
[THREAD-BRAVO // KAMEA]
Agrippa Planetary Kamea Benchmark vs Cicada Field Resonance
Pushes historical Saturn (Order 3) and Solar (Order 6) squares through the Modulo 29 Sieve.
"""

import numpy as np

class AgrippaBenchmark:
    def __init__(self):
        # Saturn Kamea (Order 3): Classic Sequential [1...9], Sums to 15
        self.saturn_kamea = np.array([
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
        ])
        
        # Solar Kamea (Order 6): Classic Sequential [1...36], Sums to 111
        self.solar_kamea = np.array([
            [6,  32,  3, 34, 35,  1],
            [7,  11, 27, 28,  8, 30],
            [19, 14, 16, 15, 23, 24],
            [18, 20, 22, 21, 17, 13],
            [25, 29, 10,  9, 26, 12],
            [36,  5, 33,  4,  2, 31]
        ])
        
        self.modulo_field = 29
        
    def analyze_saturn(self):
        print("🪐 BENCHMARKING SATURN KAMEA (ORDER 3 // CONSTANT: 15)")
        print("─" * 55)
        # Because Saturn values are all < 29, their modular residue is an exact match
        residues = self.saturn_kamea % self.modulo_field
        print("Modulo 29 Flat Residue Field:")
        for row in residues:
            print(f"  [ " + "  ".join(f"{num:2d}" for num in row) + " ]")
        print(f"Saturn Constant Mod 29 (15 mod 29): {15 % self.modulo_field}")
        
    def analyze_solar(self):
        print("\n🌞 BENCHMARKING SOLAR KAMEA (ORDER 6 // CONSTANT: 111)")
        print("─" * 55)
        # Squeeze numbers out of sequential boundaries into our runic index
        residues = self.solar_kamea % self.modulo_field
        print("Modulo 29 Compressed Residue Field:")
        for row in residues:
            print(f"  [ " + "  ".join(f"{num:2d}" for num in row) + " ]")
            
        solar_sum_residue = 111 % self.modulo_field
        print(f"Solar Constant Mod 29 (111 mod 29): {solar_sum_residue}")
        
        # Symmetrical Axis Verification
        top_left_corner = residues[0, 0]
        bottom_right_corner = residues[-1, -1]
        print(f"Corner Anti-Symmetry Check (Top Left: {top_left_corner} vs Bottom Right: {bottom_right_corner})")

if __name__ == "__main__":
    benchmark = AgrippaBenchmark()
    benchmark.analyze_saturn()
    benchmark.analyze_solar()
