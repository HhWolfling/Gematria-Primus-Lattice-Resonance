# logic/cicada_matrix_sifter.py
"""
[THREAD-CHARLIE // CICADA_ANOMALY]
Cicada 2014 Order 5 Non-Classical Matrix Sifter
Evaluates perfect palindromic reflections and extracts Modulo 29 runic signatures.
"""

import numpy as np

class CicadaMatrixSifter:
    def __init__(self):
        # The exact matrix array you provided from the 2014 puzzle
        self.matrix = np.array([
            [272, 138, 341, 131, 151],
            [366, 199, 130, 320, 18],
            [226, 245, 91, 245, 226],
            [18, 320, 130, 199, 366],
            [151, 131, 341, 138, 272]
        ])
        self.target_constant = 1033
        self.modulo_field = 29

    def evaluate_magic_properties(self):
        print("🔢 EVALUATING MATRIX BALANCES (TARGET: 1033)")
        print("─" * 50)
        
        row_sums = np.sum(self.matrix, axis=1)
        col_sums = np.sum(self.matrix, axis=0)
        diag_main = np.trace(self.matrix)
        diag_anti = np.trace(np.fliplr(self.matrix))
        
        print(f"Row Sums:    {row_sums} -> All match? {np.all(row_sums == self.target_constant)}")
        print(f"Col Sums:    {col_sums} -> All match? {np.all(col_sums == self.target_constant)}")
        print(f"Main Diag:   {diag_main} -> Matches? {diag_main == self.target_constant}")
        print(f"Anti Diag:   {diag_anti} -> Matches? {diag_anti == self.target_constant}")

    def evaluate_crab_canon_symmetries(self):
        print("\n🪞 EVALUATING CRAB CANON PALINDROMIC SYMMETRIES")
        print("─" * 50)
        
        # Symmetries checking via inverted coordinate arrays
        row_1_5_match = np.all(self.matrix[0] == self.matrix[4][::-1])
        row_2_4_match = np.all(self.matrix[1] == self.matrix[3][::-1])
        center_palindrome = np.all(self.matrix[2] == self.matrix[2][::-1])
        
        print(f"Row 1 ⇌ Row 5 Reverse Mirror: {row_1_5_match}")
        print(f"Row 2 ⇌ Row 4 Reverse Mirror: {row_2_4_match}")
        print(f"Row 3 Internal Palindrome:     {center_palindrome}")

    def extract_modulo_residues(self):
        print(f"\n🔮 EXTRACTING MODULO {self.modulo_field} RUNIC RESIDUES")
        print("─" * 50)
        
        runic_residues = self.matrix % self.modulo_field
        
        print("Residue Matrix Grid:")
        for row in runic_residues:
            print(f"  [ " + "  ".join(f"{num:2d}" for num in row) + " ]")
            
        print(f"\nCenter Node Residue (91 mod 29): {91 % self.modulo_field}")
        master_sum_residue = self.target_constant % self.modulo_field
        print(f"Master Sum Residue (1033 mod 29): {master_sum_residue}")

if __name__ == "__main__":
    sifter = CicadaMatrixSifter()
    sifter.evaluate_magic_properties()
    sifter.evaluate_crab_canon_symmetries()
    sifter.extract_modulo_residues()
