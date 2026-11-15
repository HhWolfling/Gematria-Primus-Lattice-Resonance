# logic/agrippa_solar_runic.py
"""
[THREAD-BRAVO // KAMEA]
Agrippa Solar Kamea Order 6 Runic Mapping Engine
Translates the Modulo 29 residues of the ancient Solar grid into Gematria Primus text.
"""

class SolarRunicMapper:
    def __init__(self):
        # The Modulo 29 Alphabet Ring Dictionary mapping index to Rune Glyph & Phonetic value
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

        # Agrippa's Order 6 Solar Kamea stored as a flat string (Magic Constant = 111)
        flat_solar = (
            "6 32 3 34 35 1 "
            "7 11 27 28 8 30 "
            "19 14 16 15 23 24 "
            "18 20 22 21 17 13 "
            "25 29 10 9 26 12 "
            "36 5 33 4 2 31"
        )

        nums = [int(x) % 29 for x in flat_solar.split()]
        self.solar_matrix = [nums[i:i + 6] for i in range(0, 36, 6)]

    def print_solar_tapestry(self):
        print("🌞 AGRIPPA SOLAR KAMEA RUNIC TAPESTRY (MODULO 29) 🌞")
        print("═" * 55)

        for row in self.solar_matrix:
            rune_row = []
            phonetic_row = []
            for val in row:
                rune, phon = self.gematria_ring.get(val, ("?", "?"))
                rune_row.append(rune)
                phonetic_row.append(f"{phon:^4}")

            print("   [ " + "  ".join(rune_row) + " ]   ⇌   " + "".join(phonetic_row))

        print("═" * 55)
        solar_sum_residue = 111 % 29
        rune_const, phon_const = self.gematria_ring[solar_sum_residue]
        print(f"Solar Constant (111 mod 29): Index {solar_sum_residue} ⇌ {rune_const} ({phon_const})")

if __name__ == "__main__":
    mapper = SolarRunicMapper()
    mapper.print_solar_tapestry()
