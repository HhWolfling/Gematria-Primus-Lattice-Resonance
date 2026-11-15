# swarms/companion_matrix_collision.py
"""
[THREAD-CHARLIE // CICADA_ANOMALY]
Companion Matrix Collision & Dual-Square 12-House Spin
Collides the Order 5 (1033) and Order 5 (3301) Cicada magic squares via
bitwise XOR, modular subtraction, and 180°/360° axial chord extraction.
"""

import math

class CompanionMatrixCollider:
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

        # Square A: Constant 1033
        self.sq_1033 = [
            int(x) for x in (
                "272 138 401 131 151 "
                "226 184 217 204 202 "
                "245 201 141 201 245 "
                "202 204 217 184 226 "
                "151 131 401 138 272"
            ).split()
        ]

        # Square B: Constant 3301 (from Page 16)
        self.sq_3301 = [
            int(x) for x in (
                "434 1311 312 278 966 "
                "204 812 934 280 1071 "
                "626 620 809 620 626 "
                "1071 280 934 812 204 "
                "966 278 312 1311 434"
            ).split()
        ]

    def _to_grid(self, flat_list):
        return [flat_list[i:i + 5] for i in range(0, 25, 5)]

    def _chord_at_angle(self, grid, house_idx):
        center = 2.0
        angle_rad = math.radians(house_idx * 30)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)

        spun = [list(range(5)) for _ in range(5)]
        for r in range(5):
            for c in range(5):
                proj = round(((c - center) * cos_a - (r - center) * sin_a) * house_idx)
                spun[r][c] = ((grid[r][c] % self.mod_field) + proj) % self.mod_field

        diag_main = [spun[i][i] for i in range(5)]
        diag_anti = [spun[i][4 - i] for i in range(5)]
        chord = [(diag_main[i] + diag_anti[i]) % self.mod_field for i in range(5)]
        runes = "".join(self.gematria_ring[v][0] for v in chord)
        phons = "-".join(self.gematria_ring[v][1] for v in chord)
        return chord, runes, phons

    def collide_squares(self):
        print("📡 COMPANION MATRIX COLLISION // 1033 vs 3301 ORDER 5 GRIDS 📡")
        print("═" * 74)

        # 1. Bitwise XOR & Differential Wave-Front
        xor_flat = [a ^ b for a, b in zip(self.sq_1033, self.sq_3301)]
        diff_flat = [abs(b - a) for a, b in zip(self.sq_1033, self.sq_3301)]

        print("\n[1] BITWISE XOR WAVE-FRONT (1033 ^ 3301) MOD 29:")
        for r in range(5):
            row_vals = [v % self.mod_field for v in xor_flat[r * 5:(r + 1) * 5]]
            runes = "  ".join(self.gematria_ring[v][0] for v in row_vals)
            print(f"   Row {r + 1}: {row_vals}  ⇌  [ {runes} ]")

        # 2. Check 180° (House 6) & 360° (House 12) Axial Chords for both squares
        grid_1033 = self._to_grid(self.sq_1033)
        grid_3301 = self._to_grid(self.sq_3301)

        c1, r_1033, p_1033 = self._chord_at_angle(grid_1033, 6)
        c2, r_3301, p_3301 = self._chord_at_angle(grid_3301, 6)

        print("\n[2] POLAR AXIS CHORDS AT 180° / 360° (HOUSE 6 & 12):")
        print(f"   1033 Square Polar Chord : {r_1033}  ({p_1033})")
        print(f"   3301 Square Polar Chord : {r_3301}  ({p_3301})")

        # 3. Collide the two polar chords
        merged_chord = [(x + y) % self.mod_field for x, y in zip(c1, c2)]
        m_runes = "".join(self.gematria_ring[v][0] for v in merged_chord)
        m_phons = "-".join(self.gematria_ring[v][1] for v in merged_chord)

        xor_mass = sum(xor_flat)
        print("\n" + "─" * 74)
        print(f"   [+] Merged 180°/360° Polar Chord : {m_runes}  ({m_phons})")
        print(f"   [+] Total Bitwise XOR Mass       : {xor_mass} (Mod 29 = {xor_mass % self.mod_field})")
        print(f"   [+] Total Differential Mass      : {sum(diff_flat)} (Mod 29 = {sum(diff_flat) % self.mod_field})")
        print("═" * 74)

if __name__ == "__main__":
    collider = CompanionMatrixCollider()
    collider.collide_squares()
