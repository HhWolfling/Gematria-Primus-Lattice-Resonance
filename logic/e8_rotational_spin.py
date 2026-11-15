# logic/e8_rotational_spin.py
"""
[THREAD-BRAVO // KAMEA]
E8 Lie Group Rotational Spin & 12-House Crystal Lattice Tower
Rotates compressed Modulo 29 planetary Kameas and the Cicada 1033 grid across
the 12 astronomical houses (30° to 360°) to project multi-dimensional runic keys.
"""

import math

class E8RotationalSpinEngine:
    def __init__(self):
        self.mod_field = 29
        self.target_axis = 14

        # Modulo 29 Gematria Primus Ring (with intentional twin-pair doublets)
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

        # Flat-string matrix definitions (syntax-immune)
        self.matrices = {
            "AGRIPPA MARS (Order 5 // Constant: 65)": (5, (
                "11 24 7 20 3 "
                "4 12 25 8 16 "
                "17 5 13 21 9 "
                "10 18 1 14 22 "
                "23 6 19 2 15"
            )),
            "AGRIPPA SOLAR (Order 6 // Constant: 111)": (6, (
                "6 32 3 34 35 1 "
                "7 11 27 28 8 30 "
                "19 14 16 15 23 24 "
                "18 20 22 21 17 13 "
                "25 29 10 9 26 12 "
                "36 5 33 4 2 31"
            )),
            "CICADA 1033 (Order 5 // Constant: 1033)": (5, (
                "272 138 401 131 151 "
                "226 184 217 204 202 "
                "245 201 141 201 245 "
                "202 204 217 184 226 "
                "151 131 401 138 272"
            ))
        }

    def _parse_grid(self, order, flat_str):
        nums = [int(x) % self.mod_field for x in flat_str.split()]
        return [nums[i:i + order] for i in range(0, order * order, order)]

    def _rotate_house(self, grid, house_idx):
        """
        Applies a 12-house Poincaré-style angular phase rotation (house_idx * 30°)
        weighted by radial distance from the matrix center.
        """
        n = len(grid)
        center = (n - 1) / 2.0
        angle_rad = math.radians(house_idx * 30)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)

        spun = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                dx = c - center
                dy = r - center
                # E8-inspired angular projection phase shift
                proj = round((dx * cos_a - dy * sin_a) * house_idx)
                spun[r][c] = (grid[r][c] + proj) % self.mod_field
        return spun

    def spin_tower(self):
        print("🌀 E8 LIE GROUP ROTATIONAL SPIN // 12-HOUSE CRYSTAL TOWER 🌀")
        print("═" * 74)

        for label, (order, flat_str) in self.matrices.items():
            base_grid = self._parse_grid(order, flat_str)
            print(f"\n🏛️  SPINNING MATRIX: {label}")
            print("─" * 74)

            tower_mass = 0
            for house in range(1, 13):
                deg = house * 30
                spun_grid = self._rotate_house(base_grid, house)

                # Extract Primary Diagonal (\) & Counter Diagonal (/)
                diag_main = [spun_grid[i][i] for i in range(order)]
                diag_anti = [spun_grid[i][order - 1 - i] for i in range(order)]

                # Fold both diagonals via Modulo 29 interference
                lattice_chord = [(diag_main[i] + diag_anti[i]) % self.mod_field for i in range(order)]
                chord_sum = sum(lattice_chord)
                tower_mass += chord_sum

                runes = "".join(self.gematria_ring[v][0] for v in lattice_chord)
                phons = "-".join(self.gematria_ring[v][1] for v in lattice_chord)

                print(f"   House {house:2d} ({deg:3d}°) │ Chord: {runes:<7} │ {phons:<24} │ Sum Mod 29: {chord_sum % self.mod_field:2d}")

            tower_res = tower_mass % self.mod_field
            t_rune, t_phon = self.gematria_ring[tower_res]
            delta = abs(tower_res - self.target_axis)
            print("─" * 74)
            print(f"   [+] 12-House Tower Cumulative Mass: {tower_mass}")
            print(f"   [+] Final Tower Residue Mod 29: {tower_res} ⇌ {t_rune} ({t_phon}) │ Delta to Axis 14: {delta} Steps")

        print("\n" + "═" * 74)
        print("[+] E8 12-HOUSE CRYSTAL LATTICE TOWER PROJECTION COMPLETE.")

if __name__ == "__main__":
    engine = E8RotationalSpinEngine()
    engine.spin_tower()
