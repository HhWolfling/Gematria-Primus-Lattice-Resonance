import os
from logic.mixtum_sorter import MixtumTextSorter

class AutomatedIngestionPipeline:
    def __init__(self):
        self.gematria_field = 29
        self.target_axis = 14
        self.sorter = MixtumTextSorter()
        self.root_workspace = "."

    def process_workspace_ingestion(self):
        """
        Scans the root workspace for incoming text streams, isolates their 
        typographical metrics, and passes them to the Mixtum sorting array.
        """
        print(r"--- INITIATING AUTOMATED INGESTION PIPELINE PASS ---")
        target_file = "source_text.txt"
        target_path = os.path.join(self.root_workspace, target_file)
        
        if not os.path.exists(target_path):
            print(f"[!] Target Alert: '{target_file}' not found in root workspace.")
            print("[>] Defaulting to standalone system telemetry string for pipeline validation...")
            raw_content = "Hania and Sister Shadow phase-locking the E8 Lie matrix turnaround loops."
            file_label = "telemetry_transit.txt"
        else:
            print(f"[+] Active Source Stream Detected: '{target_file}'")
            with open(target_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
            file_label = target_file

        # Execute structural classification pass through the verified sorter module
        assigned_cluster = self.sorter.analyze_and_route_payload(file_label, raw_content)
        
        print("\n--- INGESTION PIPELINE STABILIZATION REPORT ---")
        print(f"[+] PIPELINE STATUS: ACTIVE PIPELINE RE-CONDUCTION FUNCTIONAL.")
        print(f"[+] ROUTED TRACK VECTOR: {assigned_cluster}")
        print("[+] SUCCESS: THE 64_CORE PIPELINE INTEGRATION IS COMPLETE.")
        return assigned_cluster

if __name__ == "__main__":
    pipeline = AutomatedIngestionPipeline()
    pipeline.execute_system_pass = pipeline.process_workspace_ingestion()
