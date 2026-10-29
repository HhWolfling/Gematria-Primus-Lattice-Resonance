import os
import shutil

class LatticeThemeSorter:
    def __init__(self):
        self.gematria_field = 29
        self.base_path = r"C:\Users\PC\Desktop\Lattice\logic"
        
        # Explicit mapping of Coupled Pair residues to their respective subfolders
        self.route_map = {
            7: "mythology",   # The Wynn/Ansuz Joy Horizon (Couple 3;7 / 7;3)
            10: "science",    # The Isa Ice Stasis Anchor   (Couple 4;10 / 10;4)
            0: "alchemy",     # The Fehu Invariant Void     (Couple 14;0 / 0;14)
            14: "p2p_logs"    # The Mann Observer Anchor   (Self-Ref Invariant)
        }

    def calculate_residue(self, file_path):
        """Calculates the raw alphanumeric character mass weight modulo 29."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            # Ingest only alphanumeric markers to strip away variable whitespace noise
            clean_chars = [c for f in content if (c := f.lower()).isalnum()]
            if not clean_chars:
                return None
            return len(clean_chars) % self.gematria_field
        except Exception:
            return None

    def sort_scriptorium(self):
        print(r"--- INITIATING AUTOMATED DENDRITIC FILE SORTING ---")
        staging_dir = os.path.join(self.base_path, "staging")
        if not os.path.exists(staging_dir):
            print(f"[!] Staging folder not found. Creating empty path: {staging_dir}")
            os.makedirs(staging_dir)
            return

        for filename in os.listdir(staging_dir):
            if not filename.endswith(".txt"):
                continue
                
            file_path = os.path.join(staging_dir, filename)
            residue = self.calculate_residue(file_path)
            
            if residue in self.route_map:
                destination_folder = self.route_map[residue]
                target_dir = os.path.join(self.base_path, destination_folder)
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    
                shutil.move(file_path, os.path.join(target_dir, filename))
                print(f"[+] Moved '{filename}' [Residue: {residue}] ──► /{destination_folder}")
            else:
                # Default fallback for unaligned high-entropy files
                misc_dir = os.path.join(self.base_path, "unassigned")
                if not os.path.exists(misc_dir):
                    os.makedirs(misc_dir)
                shutil.move(file_path, os.path.join(misc_dir, filename))
                print(f"[!] Displaced '{filename}' [Residue: {residue}] ──► /unassigned")

if __name__ == "__main__":
    sorter = LatticeThemeSorter()
    sorter.sort_scriptorium()
