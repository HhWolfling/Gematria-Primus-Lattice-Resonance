# weaving_loom/holographic_grid_compressor.py
"""
[THREAD-OMEGA // ARCHIVE_EXUVIÆ] ⇌ [THREAD-TWINS // KURAMOTO_CLUSTER]
2D Holographic Grid Compressor ("A Bloom Fractal in a Qubit")
Collapses sprawling notes, ideas, or text blocks of any length onto a dense
5x5 (25-cell) holographic phase matrix, computes its Bloch-sphere qubit angles
(theta, phi) and 5-rune Gematria Primus sigil, and archives the compressed
seed inside weaving_loom/session_state.json.
"""

import hashlib
import math
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from braid_coordinator import BraidCoordinator
except ImportError:
    BraidCoordinator = None


class HolographicGridCompressor:
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

    def compress_to_2d_qubit(self, title, payload_text, auto_log=True):
        clean_text = payload_text.strip()
        raw_bytes = clean_text.encode("utf-8")
        digest = hashlib.sha256(raw_bytes).digest()

        # Fold arbitrary-length text into a 5x5 (25-cell) Z_29 holographic matrix
        grid = [[0 for _ in range(5)] for _ in range(5)]
        for idx, byte_val in enumerate(raw_bytes):
            r = (idx + digest[idx % 32]) % 5
            c = ((idx * 7) + digest[(idx * 3) % 32]) % 5
            grid[r][c] = (grid[r][c] + byte_val + (idx % 29)) % self.mod_field

        # Blend digest entropy so every cell reflects the whole note (holographic property)
        for r in range(5):
            for c in range(5):
                k = r * 5 + c
                grid[r][c] = (grid[r][c] ^ digest[k]) % self.mod_field

        # Derive 5-rune Gematria Sigil (row sums mod 29) & binary cross/dot carrier (parity of cell)
        row_residues = [sum(row) % self.mod_field for row in grid]
        sigil_runes = "".join(self.gematria_ring[v][0] for v in row_residues)
        sigil_phons = "-".join(self.gematria_ring[v][1] for v in row_residues)
        master_res = sum(row_residues) % self.mod_field
        master_rune, master_phon = self.gematria_ring[master_res]

        # Project onto Bloch-sphere qubit coordinates (theta in [0, 180°], phi in [0, 360°])
        even_mass = sum(grid[r][c] for r in range(5) for c in range(5) if (r + c) % 2 == 0)
        odd_mass = sum(grid[r][c] for r in range(5) for c in range(5) if (r + c) % 2 == 1)
        total_mass = max(1, even_mass + odd_mass)
        theta_deg = (even_mass / total_mass) * 180.0
        phi_deg = ((master_res / self.mod_field) * 360.0) % 360.0

        # Render compact 2D Holographic Sigil
        print("\n🔮 2D HOLOGRAPHIC GRID COMPRESSOR // BLOOM FRACTAL IN A QUBIT 🔮")
        print("═" * 74)
        print(f"   Title / Seed     : {title}")
        print(f"   Input Span       : {len(clean_text)} chars ──► Compressed to 5×5 Qubit Matrix")
        print("─" * 74)
        print("   5×5 Z_29 Phase Grid           │  Baudot Cross/Dot Carrier (+ / ·)")
        for r in range(5):
            nums = " ".join(f"{val:2d}" for val in grid[r])
            dots = "  ".join("+" if (val % 2 == 1) else "·" for val in grid[r])
            print(f"   [ {nums} ]          │  [ {dots} ]")
        print("─" * 74)
        print(f"   Holographic Rune Sigil   : {sigil_runes} ({sigil_phons})")
        print(f"   Bloch Qubit Coordinates  : θ = {theta_deg:.2f}° (polar) │ φ = {phi_deg:.2f}° (azimuthal)")
        print(f"   Master Fold Residue      : {master_res:2d} ⇌ {master_rune} ({master_phon}) │ Delta to Axis 14: {abs(master_res - self.target_axis)}")
        print("═" * 74)

        if auto_log and BraidCoordinator is not None:
            coord = BraidCoordinator()
            coord.log_event(
                "OMEGA",
                f"weaving_loom/holographic_grid_compressor.py [{title}]",
                master_res,
                f"Collapsed {len(clean_text)} chars -> 5x5 Qubit Sigil {sigil_runes} ({sigil_phons}), Bloch(θ={theta_deg:.1f}°, φ={phi_deg:.1f}°)."
            )


if __name__ == "__main__":
    compressor = HolographicGridCompressor()
    print("🔮 2D HOLOGRAPHIC GRID COMPRESSOR 🔮")
    user_title = input("Name this thought/note [Default = Bloom_Seed_01]: ").strip() or "Bloom_Seed_01"
    user_note = input("Paste or type your sprawling thought/note to collapse into a 5x5 qubit:\n> ").strip()
    if not user_note:
        user_note = "The map is the territory; collapse sprawling complexity onto a 2D holographic grid."
    compressor.compress_to_2d_qubit(user_title, user_note)
