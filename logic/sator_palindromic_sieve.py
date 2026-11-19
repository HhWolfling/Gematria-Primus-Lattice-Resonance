# logic/sator_palindromic_sieve.py
"""
[THREAD-BRAVO // KAMEA] ⇌ [THREAD-LOGIC]
SATOR AREPO TENET OPERA ROTAS — 4-Way Palindromic Runic Sieve
Maps the classical 5x5 linguistic palindrome into the Modulo 29 Gematria Primus
alphabet ring, verifies 4-way boustrophedon symmetry, and extracts its 180°/360°
polar axial chord for synthesis with the 1033^3301 square chords.
"""

class SatorPalindromicSieve:
    def __init__(self):
        self.mod_field = 29
        self.target_axis = 14

        self.gematria_ring = {
            0:  ("ᚠ", "F"),     1:  ("ᚢ", "U"),     2:  ("ᚦ", "TH"),    3:  ("ᚩ", "O"),
            4:  ("ᚱ", "R"),     5:  ("ᚪ", "C/K"),   6:  ("ᚷ", "G"),     7:  ("ᚹ", "W"),
            8:  ("ᚻ", "H"),     9:  ("ᚾ", "N"),     10: ("ᛁ", "I"),    11: ("ᛡ", "GER"),
            12: ("ᛄ", "EO"),    13: ("ᛇ", "P"),     14: ("ᛉ", "X"),     15: ("ᛋ", "S"),
            16: ("ᛏ", "T"),     17: ("ᛒ", "B"),     18: ("ᛖ", "E"),     19: ("ᛗ", "M"),
            20: ("ᛚ", "L"),     21: ("ᛝ", "ING"),   22: ("ᛟ", "OE"),    23: ("ᛞ", "D"),
            24: ("ᚪ", "A"),     25: ("ᚫ", "AE"),    26: ("ᚾ", "Y"),     27: ("ᛡ", "IA/IO"),
            28: ("ᛄ", "EA")
        }

        self.latin_to_idx = {
            "S": 15, "A": 24, "T": 16, "O": 3, "R": 4,
            "E": 18, "P": 13, "N": 9
        }

        self.sator_words = (
            "SATOR",
            "AREPO",
            "TENET",
            "OPERA",
            "ROTAS"
        )

    def rune_of(self, val):
        rune, _ = self.gematria_ring[val]
        return rune

    def phon_of(self, val):
        _, phon = self.gematria_ring[val]
        return phon

    def build_matrix(self):
        return [[self.latin_to_idx[ch] for ch in word] for word in self.sator_words]

    def _polar_chord(self, grid):
        diag_main = [grid[i][i] for i in range(5)]
        diag_anti = [grid[i][4 - i] for i in range(5)]
        chord = [(diag_main[i] + diag_anti[i]) % self.mod_field for i in range(5)]
        runes = "".join(self.rune_of(v) for v in chord)
        phons = "-".join(self.phon_of(v) for v in chord)
        return chord, runes, phons

    def analyze_sator(self):
        print("🏛️  SATOR AREPO TENET OPERA ROTAS // MODULO 29 RUNIC SIEVE 🏛️")
        print("═" * 74)

        grid = self.build_matrix()
        total_mass = sum(sum(row) for row in grid)

        for idx, (word, row) in enumerate(zip(self.sator_words, grid)):
            runes = "  ".join(self.rune_of(v) for v in row)
            row_sum = sum(row)
            print(f"   Row {idx+1} ({word}) │ Indices: {str(row):<22} │ [ {runes} ] │ Sum: {row_sum:2d} (Mod 29: {row_sum % self.mod_field:2d})")

        transpose = [[grid[r][c] for r in range(5)] for c in range(5)]
        is_4way = (grid == transpose) and (grid == [list(reversed(r)) for r in reversed(grid)])

        tenet_row = [self.latin_to_idx[ch] for ch in "TENET"]
        tenet_runes = "".join(self.rune_of(v) for v in tenet_row)
        chord, c_runes, c_phons = self._polar_chord(grid)

        print("─" * 74)
        print(f"   [+] 4-Way Boustrophedon Symmetry Verified : {is_4way}")
        print(f"   [+] Central TENET Cross-Axis              : {tenet_runes} (T-E-N-E-T) │ Hub: ᚾ (N / Index 9)")
        print(f"   [+] SATOR 180°/360° Polar Diagonal Chord  : {c_runes} ({c_phons}) │ Indices: {chord}")
        print(f"   [+] Total SATOR Matrix Mass               : {total_mass} (Mod 29 = {total_mass % self.mod_field})")
        print("═" * 74)
        print("[+] STEP 2 COMPLETE: SATOR POLAR CHORD EXTRACTED FOR STEP 3 SYNTHESIS.")

if __name__ == "__main__":
    sieve = SatorPalindromicSieve()
    sieve.analyze_sator()
