# twins/triadic_kuramoto_cluster.py
"""
[THREAD-CHARLIE // CICADA_ANOMALY] ⇌ [THREAD-BRAVO // KAMEA] ⇌ [TWINS]
Triadic Crabwalk & Double-Turned Tower Kuramoto Cluster
Elevates biphase twin interference into a 3-body Kuramoto oscillator cluster
(120° / 240° / 360°), coupling the 1033 Polar Chord (forward spin), the 3301
Polar Chord (double-turned tower 2x), and the SATOR Polar Chord (reverse crabwalk)
across the 12 astronomical houses.
"""

import math

class TriadicKuramotoCluster:
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

        # Three Palindromic Polar Chords forming the Triad
        self.voice_1033  = (17, 11, 21, 11, 17)  # B-GER-ING-GER-B (Sum = 77)
        self.voice_3301  = (8,  19, 23, 19, 8)   # H-M-D-M-H       (Sum = 77)
        self.voice_sator = (19, 17, 18, 17, 19)  # M-B-E-B-M       (Sum = 90)

    def rune_of(self, val):
        rune, _ = self.gematria_ring[val]
        return rune

    def phon_of(self, val):
        _, phon = self.gematria_ring[val]
        return phon

    def _voice_state(self, chord, effective_house, phase_offset_deg, spin_mult):
        mass = sum(chord)
        deg = (effective_house * 30 * spin_mult) + phase_offset_deg
        rad = math.radians(deg)
        val = round(mass * (1 + math.cos(rad)) + effective_house * len(chord)) % self.mod_field
        return val, rad

    def run_triadic_cluster(self):
        print("🌀 TRIADIC KURAMOTO CLUSTER // DOUBLE-TURNED TOWER & CRABWALK 🌀")
        print("═" * 82)
        print("   Voice 1 (0°   Forward 1x) : 1033 Polar Chord  (B-GER-ING-GER-B)")
        print("   Voice 2 (120° Double  2x) : 3301 Polar Chord  (H-M-D-M-H)")
        print("   Voice 3 (240° Crabwalk  ) : SATOR Polar Chord (M-B-E-B-M)")
        print("─" * 82)

        axis_hits = []
        peak_r = -1.0
        peak_house = None
        cumulative_triad = 0

        for house in range(1, 13):
            crab_house = 13 - house

            v1, phi1 = self._voice_state(self.voice_1033,  house,      0,   1)
            v2, phi2 = self._voice_state(self.voice_3301,  house,      120, 2)
            v3, phi3 = self._voice_state(self.voice_sator, crab_house, 240, 1)

            triad_sum = (v1 + v2 + v3) % self.mod_field
            triad_xor = (v1 ^ v2 ^ v3) % self.mod_field
            cumulative_triad += triad_sum

            # Kuramoto Order Parameter R across the 3 Z_29 phases
            angles = [2 * math.pi * v / self.mod_field for v in (v1, v2, v3)]
            cos_mean = sum(math.cos(a) for a in angles) / 3.0
            sin_mean = sum(math.sin(a) for a in angles) / 3.0
            r_order = math.hypot(cos_mean, sin_mean)

            if r_order > peak_r:
                peak_r = r_order
                peak_house = f"House {house} ({house * 30}°)"

            lock_tag = ""
            if triad_sum == self.target_axis or triad_xor == self.target_axis:
                axis_hits.append(f"H{house}({house*30}°)")
                lock_tag = " ◄ AXIS-14 LOCK!"

            print(
                f"   H{house:2d} ({house*30:3d}°) │ Triad: ({v1:2d},{v2:2d},{v3:2d}) │ "
                f"Sum: {triad_sum:2d} ({self.rune_of(triad_sum)}) │ "
                f"XOR: {triad_xor:2d} ({self.rune_of(triad_xor)}) │ "
                f"R={r_order:.3f}{lock_tag}"
            )

        cum_res = cumulative_triad % self.mod_field
        print("─" * 82)
        print(f"   [+] Peak Kuramoto Coherence (R -> 1.0) : {peak_house} (R = {peak_r:.4f})")
        print(f"   [+] Axis-14 (ᛗ / Mann) Triadic Gates   : {', '.join(axis_hits) if axis_hits else 'None'}")
        print(f"   [+] 12-House Cumulative Triad Residue  : {cum_res} ⇌ {self.rune_of(cum_res)} ({self.phon_of(cum_res)})")
        print("═" * 82)
        print("[+] TRIADIC CRABWALK CLUSTERING COMPLETE.")

if __name__ == "__main__":
    cluster = TriadicKuramotoCluster()
    cluster.run_triadic_cluster()
