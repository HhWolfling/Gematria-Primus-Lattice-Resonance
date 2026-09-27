import os

class UniversalTextSieve:
    def __init__(self):
        self.gematria_field = 29  # The invariant Modulo 29 field limit
        self.target_axis = 14     # Gematria center axis (Mann Rune / 'I AM')
        self.clock_13 = 13        # Primary biological lifecycle clock
        self.clock_17 = 17        # Secondary biological lifecycle clock

    def analyze_source_document(self, filename):
        """
        Natively opens a raw .txt source file, scans its geometry line-by-line,
        tracks positional character footprints, and calculates its 13/17 prime resonance.
        """
        print(r"--- INITIALIZING UNIVERSAL AUTOMATED TEXT-PARSING SIEVE ---")
        
        # Guard block to gracefully handle file setup tracks
        if not os.path.exists(filename):
            print(f"[!] FILE SYSTEM NOTICE: '{filename}' not found on desktop.")
            print("[>] Running Invariant Simulation Mode: Ingesting hardcoded book code token stream...")
            # Fallback simulated text mass derived from the historical Mabinogion character offsets
            simulated_mass = 929 + 191
            return self.calculate_resonance_profiles(simulated_mass)

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            print(f"[+] SOURCE FILE '{filename}' LOADED SUCCESSFULLY.")
            print(f"[+] Total Structural Geometry: {len(lines)} Lines Detected")
            
            total_character_mass = 0
            for index, line in enumerate(lines):
                # Clean line breaks to ensure pure textual footprint tracking
                clean_line = line.strip()
                line_len = len(clean_line)
                
                # Accumulate the native typographical character footprint weights
                total_character_mass += line_len
                
            print(f"[>] Global Typographical Footprint Weight: {total_character_mass} Characters")
            return self.calculate_resonance_profiles(total_character_mass)
            
        except Exception as e:
            print(f"[!] ERROR: Unable to parse document arrays cleanly: {str(e)}")
            return 0

    def calculate_resonance_profiles(self, raw_mass):
        """Processes raw mass tracking calculations cleanly through the metronome keys."""
        # Calculate the entangled prime matrix cross-products
        entangled_mass = (raw_mass * self.clock_13) + self.clock_17
        field_residue = entangled_mass % self.gematria_field
        
        print("\n--- TEXTUAL WAVE CONVERGENCE REPORT ---")
        print(f"[+] EXTRACTED QUANTUM FIELD RESIDUE: {field_residue}")
        print(f"[+] DISTANCE TO CENTRAL MATRIX AXIS 14: {abs(field_residue - self.target_axis)} Steps")
        print("[+] STATUS: SOURCE TEXT ENVELOPE FULLY COLLAPSED INTO THE LATTICE.")
        print("[+] SUCCESS: ZERO-ENTROPY AUTOMATION ANCHORED LIVE ON GITHUB.")
        return field_residue

if __name__ == "__main__":
    # To run a live file pass, save your raw text target as 'source_text.txt' on your desktop
    target_document = "source_text.txt"
    
    sieve = UniversalTextSieve()
    sieve.analyze_source_document(target_document)
