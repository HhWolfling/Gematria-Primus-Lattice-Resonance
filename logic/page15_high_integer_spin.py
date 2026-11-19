# logic/page15_high_integer_spin.py
"""
[THREAD-CHARLIE // CICADA_ANOMALY] ⇌ [THREAD-BRAVO // KAMEA]
Page 15 High-Integer 4x4 Grid — E8 12-House Rotational Tower Spin
Compresses the 16 high-integer values from Liber Primus Page 15 (1820..3258)
through the Modulo 29 Gematria Primus ring and spins them across the 12
astronomical houses (30° to 360°) to test rotational torque and polar chords.
"""

import math

class Page15HighIntegerSpin:
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

        # Page 15 4x4 High-Integer Lattice stored as a flat string
        flat_page15 = (
            "3258 3233 3076 3051 "
            "2846 2821 2664 2639 "
            "2434 2409 2252 2227 "
            "2022 1997 1840 1820"
        )

        self.raw_nums = [int(x) for x in flat_page15.split()]
        self.base_grid = [
            [self.raw_nums[r * 4 + c] % self.mod_field for c in range(4)]
            for r in range(4)
        ]

    def rune_of(self, val):
        rune, _ = self.gematria_ring[val]
        return rune

    def phon_of(self, val):
        _, phon = self.gematria_ring[val]
        return phon

    def _rotate_house(self, house_idx):
        center = 1.5
        angle_rad = math.radians(house_idx * 30)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)

        spun = [list(range(4)) for _ in range(4)]
        for r in range(4):
            for c in range(4):
                proj = round(((c - center) * cos_a - (r - center) * sin_a) * house_idx)
                spun[r][c] = (self.base_grid[r][c] + proj) % self.mod_field
        return spun

    def run_tower_spin(self):
        print("🗼 PAGE 15 HIGH-INTEGER 4x4 LATTICE // E8 12-HOUSE TOWER SPIN 🗼")
        print("═" * 76)
        print("   Base Modulo 29 Compressed 4x4 Grid:")
        for r in range(4):
            row_vals = self.base_grid[r]
            runes = "  ".join(self.rune_of(v) for v in row_vals)
            print(f"   Row {r+1}: {str(row_vals):<18} ⇌  [ {runes} ]")

        print("─" * 76)
        tower_mass = 0
        house_sums = set()

        for house in range(1, 13):
            deg = house * 30
            spun = self._rotate_house(house)

            diag_main = [spun[i][i] for i in range(4)]
            diag_anti = [spun[i][3 - i] for i in range(4)]
            chord = [(diag_main[i] + diag_anti[i]) % self.mod_field for i in range(4)]

            chord_sum = sum(chord)
            sum_mod = chord_sum % self.mod_field
            house_sums.add(sum_mod)
            tower_mass += chord_sum

            runes = "".join(self.rune_of(v) for v in chord)
            phons = "-".join(self.phon_of(v) for v in chord)
            is_pal = (chord == list(reversed(chord)))
            pal_tag = " [PALINDROME]" if is_pal else ""

            print(f"   House {house:2d} ({deg:3d}°) │ Chord: {runes:<6} │ {phons:<22} │ Sum Mod 29: {sum_mod:2d}{pal_tag}")

        tower_res = tower_mass % self.mod_field
        print("─" * 76)
        print(f"   [+] Raw 16-Cell Sum              : {sum(self.raw_nums)} (Mod 29 = {sum(self.raw_nums) % self.mod_field})")
        print(f"   [+] Unique House Sum Residues    : {sorted(house_sums)} ({'ZERO-TORQUE LOCK' if len(house_sums) == 1 else 'DYNAMIC WAVE'})")
        print(f"   [+] 12-House Cumulative Residue  : {tower_res} ⇌ {self.rune_of(tower_res)} ({self.phon_of(tower_res)}) │ Delta to Axis 14: {abs(tower_res - self.target_axis)}")
        print("═" * 76)

if __name__ == "__main__":
    spin = Page15HighIntegerSpin()
    spin.run_tower_spin()
