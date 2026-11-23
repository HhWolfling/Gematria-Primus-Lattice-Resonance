# parsers/blake_oak_mayfly_sieve.py
"""
[THREAD-DELTA // PARSER_SIGHT] ⇌ [THREAD-MYTHOS]
William Blake Hovering Figure, Dual Oak Trees & Page 73/74 Spray-Paint Mayfly Sieve
Unifies the three uncracked visual layers of Liber Primus:
  1. William Blake supine/hovering figure & Zoa constants (Tharmas=13, Urizen=17)
  2. Dual Oak Tree Gaussian differential residual mass (2242 -> Mod 29 = 9)
  3. Page 73/74 dithered "spray-paint" mayfly & 8-vein wing coordinate map
"""

import os
import sys

# Allow direct import of BraidCoordinator from weaving_loom/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "weaving_loom")))
try:
    from braid_coordinator import BraidCoordinator
except ImportError:
    BraidCoordinator = None


class BlakeOakMayflySieve:
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

        # Layer 1: Blake Supine / Hovering Angel-Dragon Zoa Constants
        self.blake_zoas = (13, 17, 4, 2)  # Tharmas=13, Urizen=17, 4 Zoas, 2 Biphase Bodies

        # Layer 2: Dual Oak Tree (Sharp - Blurred) Extracted Pixel Differential Mass
        self.oak_diff_mass = 2242

        # Layer 3: Page 73/74 Wing Venation & Spray-Paint Mayfly Coordinates
        self.wing_vein_labels = ("SC", "R1", "R2+3", "R5", "M1", "M2", "CU1B", "1A")
        self.terminal_pages = (73, 74)

    def rune_of(self, val):
        rune, _ = self.gematria_ring[val]
        return rune

    def phon_of(self, val):
        _, phon = self.gematria_ring[val]
        return phon

    def analyze_visual_triad(self):
        print("🎨 BLAKE / DUAL OAK / SPRAY-PAINT MAYFLY VISUAL ARCHAEOLOGY SIEVE 🎨")
        print("═" * 78)

        # 1. Blake Layer
        blake_mass = sum(self.blake_zoas) * 14
        blake_res = blake_mass % self.mod_field

        # 2. Dual Oak Differential Layer
        oak_res = self.oak_diff_mass % self.mod_field

        # 3. Page 73/74 Spray-Paint Mayfly & 8-Vein Wing Layer
        vein_ascii_mass = sum(ord(ch) for label in self.wing_vein_labels for ch in label)
        mayfly_mass = (vein_ascii_mass * self.terminal_pages[0]) + self.terminal_pages[1]
        mayfly_res = mayfly_mass % self.mod_field

        # 4. Unified Visual Triad Collision (Sum & XOR Modulo 29)
        triad_sum = (blake_res + oak_res + mayfly_res) % self.mod_field
        triad_xor = (blake_res ^ oak_res ^ mayfly_res) % self.mod_field

        print(f"   1. Blake Hovering Figure (Zoas {self.blake_zoas})")
        print(f"      Mass: {blake_mass:<8} │ Mod 29: {blake_res:2d} ⇌ {self.rune_of(blake_res)} ({self.phon_of(blake_res)})")

        print(f"   2. Dual Oak Trees (Sharp vs. Gaussian Blur)")
        print(f"      Mass: {self.oak_diff_mass:<8} │ Mod 29: {oak_res:2d} ⇌ {self.rune_of(oak_res)} ({self.phon_of(oak_res)})")

        print(f"   3. Page 73/74 Spray-Paint Mayfly & 8-Vein Wing")
        print(f"      Mass: {mayfly_mass:<8} │ Mod 29: {mayfly_res:2d} ⇌ {self.rune_of(mayfly_res)} ({self.phon_of(mayfly_res)})")

        print("─" * 78)
        print(f"   [+] Unified Visual Triad Sum Mod 29 : {triad_sum:2d} ⇌ {self.rune_of(triad_sum)} ({self.phon_of(triad_sum)}) │ Delta to Axis 14: {abs(triad_sum - self.target_axis)}")
        print(f"   [+] Unified Visual Triad XOR Mod 29 : {triad_xor:2d} ⇌ {self.rune_of(triad_xor)} ({self.phon_of(triad_xor)}) │ Delta to Axis 14: {abs(triad_xor - self.target_axis)}")
        print("═" * 78)

        # Auto-log milestone to weaving_loom/session_state.json if available
        if BraidCoordinator is not None:
            coordinator = BraidCoordinator()
            coordinator.log_event(
                "DELTA",
                "parsers/blake_oak_mayfly_sieve.py",
                triad_sum,
                f"Blake/Oak/Mayfly visual triad unified: Sum Mod29={triad_sum} ({self.phon_of(triad_sum)}), XOR Mod29={triad_xor} ({self.phon_of(triad_xor)})."
            )


if __name__ == "__main__":
    sieve = BlakeOakMayflySieve()
    sieve.analyze_visual_triad()
