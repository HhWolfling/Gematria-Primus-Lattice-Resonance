# logic/agrippa_planetary_kameas.py
"""
[THREAD-BRAVO // KAMEA]
Agrippa Classical Planetary Kameas Runic Mapping Engine
Compresses Saturn (Order 3), Jupiter (Order 4), Mars (Order 5), Solar (Order 6),
and Venus (Order 7) through the Modulo 29 Gematria Primus Ring.
"""

class PlanetaryKameaEngine:
    def __init__(self):
        self.gematria_ring = {
            0:  ("ᚠ", "F"),     1:  ("ᚢ", "U"),     2:  ("ᚦ", "TH"),    3:  ("ᚩ", "O"),
            4:  ("ᚱ", "R"),     5:  ("ᚪ", "C/K"),   6:  ("ᚷ", "G"),     7:  ("ᚹ", "W"),
            8:  ("ᚻ", "H"),     9:  ("ᚾ", "N"),     10: ("ᛁ", "I"),    11: ("ᛡ", "GER"),
            12: ("ᛄ", "EO"),    13: ("ᛇ", "P"),     14: ("ᛉ", "X"),     15: ("ᛋ", "S"),
            16: ("ᛏ", "T"),     17: ("ᛒ", "B"),     18: ("ᛖ", "E"),     19: ("ᛗ", "M"),
            20: ("ᛚ", "L"),     21: ("ᛝ", "ING"),   22: ("ᛟ", "OE"),    23: ("ᛞ", "D"),
            24: ("ᚪ", "A"),     25: ("Æ", "AE"),    26: ("ᚾ", "Y"),     27: ("ᛡ", "IA/IO"),
            28: ("ᛄ", "EA")
        }

        # Classical Agrippa Magic Squares stored as flat space-separated strings
        self.kameas = {
            "SATURN (Order 3 // Constant: 15)": (3, 15, (
                "4 9 2 "
                "3 5 7 "
                "8 1 6"
            )),
            "JUPITER (Order 4 // Constant: 34)": (4, 34, (
                "4 14 15 1 "
                "9 7 6 12 "
                "5 11 10 8 "
                "16 2 3 13"
            )),
            "MARS (Order 5 // Constant: 65)": (5, 65, (
                "11 24 7 20 3 "
                "4 12 25 8 16 "
                "17 5 13 21 9 "
                "10 18 1 14 22 "
                "23 6 19 2 15"
            )),
            "SOLAR (Order 6 // Constant: 111)": (6, 111, (
                "6 32 3 34 35 1 "
                "7 11 27 28 8 30 "
                "19 14 16 15 23 24 "
                "18 20 22 21 17 13 "
                "25 29 10 9 26 12 "
                "36 5 33 4 2 31"
            )),
            "VENUS (Order 7 // Constant: 175)": (7, 175, (
                "22 47 16 41 10 35 4 "
                "5 23 48 17 42 11 29 "
                "30 6 24 49 18 36 12 "
                "13 31 7 25 43 19 37 "
                "38 14 32 1 26 44 20 "
                "21 39 8 33 2 27 45 "
                "46 15 40 9 34 3 28"
            ))
        }

    def render_all_kameas(self):
        print("🌌 AGRIPPA CLASSICAL PLANETARY KAMEAS — MODULO 29 RUNIC ATLAS 🌌")
        print("═" * 68)

        for name, (order, magic_const, flat_str) in self.kameas.items():
            nums = [int(x) % 29 for x in flat_str.split()]
            grid = [nums[i:i + order] for i in range(0, order * order, order)]

            const_res = magic_const % 29
            c_rune, c_phon = self.gematria_ring[const_res]

            print(f"\n🪐 {name}")
            print(f"   Magic Constant Mod 29: {const_res} ⇌ {c_rune} ({c_phon})")
            print("─" * 68)

            for row in grid:
                runes = [self.gematria_ring[v][0] for v in row]
                phons = [f"{self.gematria_ring[v][1]:^5}" for v in row]
                print("   [ " + "  ".join(runes) + " ]   ⇌   " + "".join(phons))

        print("\n" + "═" * 68)
        print("[+] ALL FIVE PLANETARY KAMEAS COMPRESSED & MAPPED CLEANLY.")

if __name__ == "__main__":
    engine = PlanetaryKameaEngine()
    engine.render_all_kameas()
