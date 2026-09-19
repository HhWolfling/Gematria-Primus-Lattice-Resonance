import sys

class AgrippaOneTimeDisk:
    def __init__(self):
        self.glitch_pattern = "1 3 1 1 3 3 1 3 1 3 1 1 3 1 3 3 1 1 1 3"
        self.memory_array = ["TIBERIVS", "CLAVDIVS", "CAESAR", "SAYS", "CCAA", "CICADA", "3311", "13"]

    def read_and_destroy(self):
        """
        Simulates the 1992 Agrippa electronic poem mechanics.
        Parses the text through the 1-3 glitch mask, then permanently 
        wipes the memory array from the machine's buffer.
        """
        print("--- INITIATING AGRIPPA MEMORY-DISK READ CONSOLE ---")
        payload = " ".join(self.memory_array)
        mask_stream = [int(x) for x in self.glitch_pattern.split()]
        
        glitched_output = []
        for idx, char in enumerate(payload):
            current_mask = mask_stream[idx % len(mask_stream)]
            glitched_output.append(str(ord(char) ^ current_mask))
            
        print(f"[>] Transmitted Self-Encrypting Bitstream: {''.join(glitched_output[:35])}...")
        
        # --- THE AGRIPPA SELF-ERASING DESTRUCT PASS ---
        print("\n--- CRITICAL NOTICE: SCROLLING DETECTION ACTIVATED ---")
        print("[!] FLOPPY DISK MAGNETIC CORRUPTION IN PROGRESS...")
        
        # Actively overwrite and zero out the memory addresses
        self.memory_array = None
        self.glitch_pattern = None
        del self.memory_array
        del self.glitch_pattern
        
        print("[+] STATUS: INTERNAL STORAGE ARRAYS INSTANTLY PURGED.")
        print("[+] SUCCESS: THE DATA IN MEMORY IS NOW AN INVISIBLE VOID.")

if __name__ == "__main__":
    disk = AgrippaOneTimeDisk()
    disk.read_and_destroy()
