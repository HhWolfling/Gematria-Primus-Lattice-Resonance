# logic/cicada_matrix_sifter_runic.py
"""
[THREAD-CHARLIE // CICADA_ANOMALY]
Cicada 2014 Order 5 Non-Classical Matrix Sifter
Maps Modulo 29 residues onto the Gematria Primus Runic Field.
"""

import numpy as np

class GematriaMapper:
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
        
        # The pristine residue matrix we pulled from the square (Fixed syntax error)
        self.residues = np.array([
            [11, 22, 22, 15,  6],
            [18, 25, 14,  1, 18],
            [23, 13,  4, 13, 23],
            [18,  1, 14, 25, 18],
            [ 6, 15, 22, 22, 11]
        ])

    def print_runic_tapestry(self):
        print("ᛡᛖᛉ RUNIC MATRIX TAPESTRY (MODULO 29 FIELD) ᛡᛖᛉ")
        print("═" * 50)
        
        for row in self.residues:
            rune_row = []
            phonetic_row = []
            for val in row:
                rune, phon = self.gematria_ring.get(val, ("?", "?"))
                rune_row.append(rune)
                phonetic_row.append(f"{phon:^4}")
            
            # Print the glyph lines alongside their sound weights
            print(f"   [ " + "  ".join(rune_row) + " ]   ⇌   " + "".join(phonetic_row))
            
        print("═" * 50)
        print(f"Center Core (Index 4):     {self.gematria_ring[4][0]} ({self.gematria_ring[4][1]})")
        print(f"Master Sum Key (Index 18): {self.gematria_ring[18][0]} ({self.gematria_ring[18][1]})")

if __name__ == "__main__":
    mapper = GematriaMapper()
    mapper.print_runic_tapestry()
