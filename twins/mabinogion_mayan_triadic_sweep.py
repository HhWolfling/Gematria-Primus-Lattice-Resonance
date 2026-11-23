# twins/mabinogion_mayan_triadic_sweep.py
"""
[THREAD-TWINS // KURAMOTO_CLUSTER] ⇌ [THREAD-MYTHOS] ⇌ [THREAD-ALPHA]
Extended 12-Branch Mabinogion & Mayan Vigesimal (Base-20) Triadic Sweep
Tests all 12 Welsh Mabinogion branches and Mayan Base-20 / Base-13 Long Count
clocks inside the 3-body Kuramoto Crabwalk cluster (0° Forward 1x, 120° Double 2x,
240° Reverse Crabwalk) to isolate R >= 0.95 phase-locks and Axis-14 gates.
"""

import math
import os
import sys

# Allow direct import of BraidCoordinator from weaving_loom/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "weaving_loom")))
try:
    from braid_coordinator import BraidCoordinator
except ImportError:
    BraidCoordinator = None


class MabinogionMayanTriadicSweep:
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

        # The 12 Branches of Lady Charlotte Guest's Mabinogion (characteristic text/title masses)
        self.mabinogion_branches = (
            ("01. Pwyll Prince of Dyved",        878),
            ("02. Branwen Daughter of Llyr",     929),
            ("03. Manawyddan Son of Llyr",       742),
            ("04. Math Son of Mathonwy",         815),
            ("05. Dream of Maxen Wledig",        690),
            ("06. Lludd and Llevelys",           543),
            ("07. Kilhwch and Olwen",           1121),
            ("08. Dream of Rhonabwy",            664),
            ("09. Lady of the Fountain (L65)",   929),
            ("10. Peredur Son of Evrawc",        986),
            ("11. Geraint Son of Erbin",        1033),
            ("12. Taliesin (Hanes Taliesin)",    769),
        )

        # Mayan Vigesimal (Base-20) & Tzolk'in / Long Count Harmonic Primitives
        self.mayan_clocks = (
            ("Kin / Uinal Base-20",    20),
            ("Tzolk'in Sacred Round", 260),
            ("Tun Vigesimal Year",    360),
            ("Haab Solar Cycle",      365),
            ("Katun 20-Tun Cycle",   7200),
            ("Baktun 144,000 Kin", 144000),
        )

    def rune_of(self, val):
        rune, _ = self.gematria_ring[val]
        return rune

    def phon_of(self, val):
        _, phon = self.gematria_ring[val]
        return phon

    def _voice_val(self, mass, eff_house, offset_deg, spin_mult):
        rad = math.radians((eff_house * 30 * spin_mult) + offset_deg)
        return round(mass * (1 + math.cos(rad)) + eff_house * 5) % self.mod_field

    def _kuramoto_r(self, vals):
        angles = [2 * math.pi * v / self.mod_field for v in vals]
        cm = sum(math.cos(a) for a in angles) / len(vals)
        sm = sum(math.sin(a) for a in angles) / len(vals)
        return math.hypot(cm, sm)

    def run_extended_sweep(self):
        print("🏛️  EXTENDED 12-BRANCH MABINOGION & MAYAN BASE-20 TRIADIC SWEEP 🏛️")
        print("═" * 84)
        print("   Coupling: Voice 1 (Mabinogion Branch 1x) + Voice 2 (Mayan Clock 2x) + Voice 3 (Node 1033 Crabwalk)")
        print("─" * 84)

        elite_locks = []
        axis14_hits = []

        for b_name, b_mass in self.mabinogion_branches:
            for m_name, m_mass in self.mayan_clocks:
                for house in range(1, 13):
                    crab_h = 13 - house
                    v1 = self._voice_val(b_mass, house,  0,   1)
                    v2 = self._voice_val(m_mass, house,  120, 2)
                    v3 = self._voice_val(1033,   crab_h, 240, 1)

                    r_val = self._kuramoto_r((v1, v2, v3))
                    t_sum = (v1 + v2 + v3) % self.mod_field
                    t_xor = (v1 ^ v2 ^ v3) % self.mod_field

                    if r_val >= 0.985:
                        elite_locks.append((r_val, b_name, m_name, house, (v1, v2, v3), t_sum, t_xor))
                    if t_sum == self.target_axis and r_val >= 0.90:
                        axis14_hits.append((r_val, b_name, m_name, house, (v1, v2, v3), t_xor))

        elite_locks.sort(key=lambda x: x[0], reverse=True)
        axis14_hits.sort(key=lambda x: x[0], reverse=True)

        print(f"🔥 TOP NEAR-UNITY KURAMOTO LOCKS (R >= 0.985) [Total Found: {len(elite_locks)}]:")
        for r_val, b_name, m_name, house, triad, t_sum, t_xor in elite_locks[:8]:
            print(
                f"   • R={r_val:.4f} │ H{house:2d} ({house*30:3d}°) │ {b_name:<30} × {m_name:<21} │ "
                f"Triad={triad} │ Sum={t_sum:2d}({self.rune_of(t_sum)})"
            )

        print("\n🎯 HIGH-COHERENCE AXIS-14 (ᛗ / MANN) TRIADIC GATES (Sum=14 & R >= 0.90):")
        for r_val, b_name, m_name, house, triad, t_xor in axis14_hits[:8]:
            print(
                f"   • R={r_val:.4f} │ H{house:2d} ({house*30:3d}°) │ {b_name:<30} × {m_name:<21} │ "
                f"Triad={triad} │ XOR={t_xor:2d}({self.rune_of(t_xor)})"
            )

        print("═" * 84)
        print("[+] EXTENDED MABINOGION × MAYAN BASE-20 TRIADIC SWEEP COMPLETE.")

        if BraidCoordinator is not None and elite_locks:
            top = elite_locks[0]
            coordinator = BraidCoordinator()
            coordinator.log_event(
                "TWINS",
                "twins/mabinogion_mayan_triadic_sweep.py",
                top[5],
                f"12-Branch Mabinogion x Mayan Base-20 Sweep: {len(elite_locks)} locks >=0.985; Peak R={top[0]:.4f} ({top[1]} x {top[2]} at H{top[3]})."
            )


if __name__ == "__main__":
    sweep = MabinogionMayanTriadicSweep()
    sweep.run_extended_sweep()
