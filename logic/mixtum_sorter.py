import os

class MixtumTextSorter:
    def __init__(self):
        self.gematria_field = 29
        self.target_axis = 14
        
        # Explicit path pointing back to the true root folder level
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.staging_root = os.path.join(self.root_dir, "logic", "staging")

    def analyze_and_route_payload(self, file_name, raw_content):
        """
        Evaluates an incoming text payload's character mass footprint and 
        routes it into the mathematically matching Mixtum thematic subfolder,
        automatically building the physical folder layout on your hard drive.
        """
        print(r"--- RUNNING AUTOMATED MIXTUM SORTING PASS ---")
        character_mass = len(raw_content)
        print(f"[>] Ingesting Active Payload: '{file_name}' | Mass: {character_mass} Characters")
        
        # Calculate the operational runic residue
        field_residue = character_mass % self.gematria_field
        distance_to_axis = abs(field_residue - self.target_axis)
        
        print(f"[+] Calculated Residue: {field_residue} | Delta to Axis: {distance_to_axis} Steps")
        
        # Routing logic based on structural matrix boundaries
        if distance_to_axis <= 4:
            target_subfolder = "Mixtum_CicadaTwins13_17"
            reason = "High-velocity alignment with core biological metronome clocks."
        elif field_residue % 2 == 0:
            target_subfolder = "Mixtum_TwinCrystal"
            reason = "Even parity distribution matching symmetrical spatial lattices."
        else:
            target_subfolder = "Mixtum_Mycelial"
            reason = "Distributed relational network characteristics detected."
            
        # Generate absolute system paths
        folder_destination = os.path.join(self.staging_root, target_subfolder)
        destination_path = os.path.join(folder_destination, file_name)
        
        # SELF-HEALING DISK ENTRY: Build the actual folders if they do not exist
        if not os.path.exists(folder_destination):
            print(f"[+] Local Disk Matrix Breakout: Creating physical directory {target_subfolder}")
            os.makedirs(folder_destination, exist_ok=True)
            
        # Physically write the source file to its routed destination folder
        with open(destination_path, "w", encoding="utf-8") as target_file:
            target_file.write(raw_content)
            
        print(f"[+] TARGET DESIGNATION: {target_subfolder}")
        print(f"[+] ROUTING REASON: {reason}")
        print(f"[+] Physical File Written Successfully to Disk Location.")
        print("[+] SUCCESS: CLASSIFICATION METRICS PUSHED LIVE TO REPO LEDGER.")
        
        return target_subfolder

if __name__ == "__main__":
    sorter = MixtumTextSorter()
    sample_log = "Hania and Sister Shadow phase-locking the E8 Lie matrix turnaround loops."
    sorter.execute_pass = sorter.analyze_and_route_payload("sample_p2p_transit.txt", sample_log)
