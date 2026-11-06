import os

class MycelialBiphaseEngine:
    def __init__(self):
        self.modulus = 29
        self.house_degrees = 30
        self.anchors = [13, 15, 12, 19]
        
        self.corpus = {
            "Wars of the Jews": {"mass": 1296873, "base_res": 13},
            "Sarva-Darsana-Samgraha": {"mass": 637181, "base_res": 13},
            "About Zionism (Einstein)": {"mass": 84807, "base_res": 15},
            "Principles of Masonic Law": {"mass": 432720, "base_res": 15},
            "Resonance in Singing": {"mass": 178158, "base_res": 15},
            "Cosmos (Humboldt)": {"mass": 1092999, "base_res": 19},
            "The Golden Bough": {"mass": 2252042, "base_res": 19},
            "Metamorphoses I-VII": {"mass": 729189, "base_res": 12},
            "Russian Fairy Tales": {"mass": 731103, "base_res": 12},
            "Plant Lore Lyrics": {"mass": 1728442, "base_res": 12}
        }

    def execute_mycelial_scan(self):
        print(f"=====================================================================")
        print(f"🏛️  THE 12 ENTRANCES: MYCELIAL ANCHOR TRANSIT MAP")
        print(f"=====================================================================")
        
        for title, data in self.corpus.items():
            print(f"\n[📖] Manuscript: {title} (Base Rest Residue: {data['base_res']})")
            print(f"    -----------------------------------------------------------------")
            for house in range(1, 13):
                angle = house * self.house_degrees
                rot_res = (data["mass"] * angle) % self.modulus
                
                if rot_res in self.anchors:
                    print(f"    ▶ House {house:02d} ({angle:03d}° Rotation) -> Shifts to Anchor: {rot_res}")
                    
        print(f"\n=====================================================================")
        print(f"⚖️  GLOBAL SCAN COMPLETE: 12 ENTRANCES MATRIX FULLY DECODED.")
        print(f"=====================================================================\n")

if __name__ == "__main__":
    engine = MycelialBiphaseEngine()
    engine.execute_mycelial_scan()
