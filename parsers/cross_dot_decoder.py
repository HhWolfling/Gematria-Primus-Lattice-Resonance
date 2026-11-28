# parsers/cross_dot_decoder.py
"""
[THREAD-DELTA // PARSER_SIGHT] ⇌ [THREAD-CHARLIE // CICADA_ANOMALY]
Orthodox Cross 25-Bit (5x5) Auto-Centered Multi-Mode Decoder (Pages 17, 18, 19, 21)
Auto-locates the exact centroids of the upper-right and lower-left Orthodox
crosses before applying 180° rotational XOR, decodes across 4 channels, and
automatically logs every page result into weaving_loom/session_state.json.
"""

import os
import sys

try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

# Connect directly to weaving_loom/braid_coordinator.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "weaving_loom")))
try:
    from braid_coordinator import BraidCoordinator
except ImportError:
    BraidCoordinator = None


class CrossDotDecoder:
    def __init__(self):
        self.mod_field = 29
        self.target_axis = 14

        self.ita2_to_char = {
            "00000": "·", "00100": " ", "10111": "Q", "10011": "W",
            "00001": "E", "01010": "R", "10000": "T", "10101": "Y",
            "00111": "U", "00110": "I", "11000": "O", "10110": "P",
            "00011": "A", "00101": "S", "01001": "D", "01101": "F",
            "11010": "G", "10100": "H", "01011": "J", "01111": "K",
            "10010": "L", "10001": "Z", "11101": "X", "01110": "C",
            "11110": "V", "11001": "B", "01100": "N", "11100": "M",
            "01000": "\\n", "00010": "\\r", "11011": "[FIGS]", "11111": "[LTRS]"
        }

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

    def _find_cross_patch(self, gray_img, y_range, x_range, half_box=45):
        h, w = gray_img.shape
        y0, y1 = int(h * y_range[0]), int(h * y_range[1])
        x0, x1 = int(w * x_range[0]), int(w * x_range[1])
        zone = gray_img[y0:y1, x0:x1]

        _, ink = cv2.threshold(zone, 160, 255, cv2.THRESH_BINARY_INV)
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(ink)

        best_idx = -1
        best_area = 0
        for idx in range(1, num_labels):
            area = stats[idx, cv2.CC_STAT_AREA]
            if 40 <= area <= 4000 and area > best_area:
                best_area = area
                best_idx = idx

        if best_idx == -1:
            cy, cx = (y0 + y1) // 2, (x0 + x1) // 2
        else:
            cx = x0 + int(round(centroids[best_idx][0]))
            cy = y0 + int(round(centroids[best_idx][1]))

        patch = gray_img[
            max(0, cy - half_box):min(h, cy + half_box),
            max(0, cx - half_box):min(w, cx + half_box)
        ]
        return cv2.resize(patch, (half_box * 2, half_box * 2)), (cx, cy)

    def extract_25bit_grid_from_image(self, image_path):
        if not HAS_CV2 or not os.path.exists(image_path):
            return None, None, None

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return None, None, None

        ur_crop, ur_pt = self._find_cross_patch(img, (0.12, 0.42), (0.78, 0.96), half_box=45)
        ll_crop, ll_pt = self._find_cross_patch(img, (0.55, 0.85), (0.04, 0.22), half_box=45)

        ur_rot180 = cv2.rotate(ur_crop, cv2.ROTATE_180)
        xor_diff = cv2.bitwise_xor(ll_crop, ur_rot180)
        xor_mean = float(np.mean(xor_diff))

        _, thresh = cv2.threshold(xor_diff, 65, 255, cv2.THRESH_BINARY)
        grid = []
        size = xor_diff.shape[0]
        cell = size // 5
        for r in range(5):
            row_bits = []
            for c in range(5):
                block = thresh[r * cell:(r + 1) * cell, c * cell:(c + 1) * cell]
                active_px = int(np.sum(block > 0))
                row_bits.append(1 if active_px >= 2 else 0)
            grid.append(row_bits)

        return grid, xor_mean, (ll_pt, ur_pt)

    def decode_grid(self, page_label, grid, xor_mean=None, pts=None, coordinator=None):
        print(f"\n✝️  PAGE {page_label} // AUTO-CENTERED ORTHODOX CROSS 5×5 DECODER ✝️")
        if pts is not None:
            print(f"   Cross Centroids       : Lower-Left={pts[0]} │ Upper-Right={pts[1]}")
        if xor_mean is not None:
            print(f"   Biphase 180° XOR Mean : {xor_mean:.2f} (Background Cancelled: {'YES' if xor_mean < 50 else 'CHECK'})")
        print("─" * 74)

        for r_idx, row in enumerate(grid):
            bits_str = " ".join(str(b) for b in row)
            print(f"   Row {r_idx + 1}: [ {bits_str} ]")

        row_words = ["".join(str(b) for b in row) for row in grid]
        row_text = "".join(self.ita2_to_char.get(w, "?") for w in row_words)

        col_words = ["".join(str(grid[r][c]) for r in range(5)) for c in range(5)]
        col_text = "".join(self.ita2_to_char.get(w, "?") for w in col_words)

        flat_bits = "".join(row_words)[::-1]
        rev_words = [flat_bits[i:i + 5] for i in range(0, 25, 5)]
        rev_text = "".join(self.ita2_to_char.get(w, "?") for w in rev_words)

        row_ints = [int(w, 2) % self.mod_field for w in row_words]
        runes = "".join(self.gematria_ring[v][0] for v in row_ints)
        phons = "-".join(self.gematria_ring[v][1] for v in row_ints)
        total_res = sum(row_ints) % self.mod_field
        res_rune, res_phon = self.gematria_ring[total_res]

        print("─" * 74)
        print(f"   Row-Wise ITA2 Baudot       : '{row_text}'   {row_words}")
        print(f"   Col-Wise ITA2 Baudot       : '{col_text}'   {col_words}")
        print(f"   180° Crab Canon Reversed   : '{rev_text}'   {rev_words}")
        print(f"   Gematria Primus Rune Chord : {runes} ({phons})")
        print(f"       Cumulative Mod 29 Residue  : {total_res:2d} ⇌ {res_rune} ({res_phon}) │ Delta to Axis 14: {abs(total_res - self.target_axis)}")
        print("═" * 74)

        if coordinator is not None:
            coordinator.log_event(
                "DELTA",
                f"parsers/cross_dot_decoder.py [Page {page_label}]",
                total_res,
                f"Orthodox Cross 5x5 XOR (mean={xor_mean:.2f}): Row='{row_text}', CrabRev='{rev_text}', Runes={runes} ({phons}), Mod29={total_res} ({res_phon})."
            )

    def run_all_pages(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        coordinator = BraidCoordinator() if BraidCoordinator is not None else None

        for pg in ["17", "18", "19", "21"]:
            img_path = os.path.join(base_dir, f"original_{pg}.jpg")
            if os.path.exists(img_path) and HAS_CV2:
                grid, xor_mean, pts = self.extract_25bit_grid_from_image(img_path)
                if grid is not None:
                    self.decode_grid(pg, grid, xor_mean, pts, coordinator)


if __name__ == "__main__":
    decoder = CrossDotDecoder()
    decoder.run_all_pages()
