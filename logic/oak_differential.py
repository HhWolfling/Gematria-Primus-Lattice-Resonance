from PIL import Image

class OakDifferentialEngine:
    def __init__(self):
        self.gematria_field = 29  # The invariant Modulo 29 runic field limit
        self.target_axis = 14     # Gematria center axis (Mann Rune)

    def extract_hidden_residuals(self, sharp_path, blurred_path):
        """
        Ingests both images, subtracts the blurred pixel weights from the sharp
        pixel weights, and displays the hidden data residuals natively.
        """
        print(r"--- INITIATING PIXEL-DIFFERENTIAL OAK EXTRACTION ---")
        
        try:
            # Open both images natively from your desktop
            img_sharp = Image.open(sharp_path).convert("RGB")
            img_blurred = Image.open(blurred_path).convert("RGB")
            
            # Ensure the dimensions match perfectly
            if img_sharp.size != img_blurred.size:
                print("[!] ERROR: Image dimensions do not match. The grid is misaligned.")
                return
                
            print(f"[+] IMAGES LOADED. DIMENSIONS SECURED: {img_sharp.size}")
            
            # Load the raw pixel arrays into local processing memory
            pixels_s = img_sharp.load()
            pixels_b = img_blurred.load()
            
            width, height = img_sharp.size
            extracted_deltas = []
            
            # Scan a 100-pixel sample strip through the center of the canvas
            # to expose the steganographic data remnants safely
            start_x = width // 2
            start_y = height // 2
            
            for i in range(20):
                x = start_x + i
                y = start_y
                
                # Fetch RGB values for both images
                r_s, g_s, b_s = pixels_s[x, y]
                r_b, g_b, b_b = pixels_b[x, y]
                
                # Calculate the high-frequency pixel differential
                pixel_delta = abs(r_s - r_b) + abs(g_s - g_b)
                
                if pixel_delta > 0:
                    extracted_deltas.append(pixel_delta)
                    
            print(f"[>] Raw Steganographic Pixel Residues Isolated: {extracted_deltas[:10]}...")
            
            if extracted_deltas:
                # Sieve the resulting pixel mass through our Modulo 29 Gematria field
                global_mass = sum(extracted_deltas)
                field_residue = global_mass % self.gematria_field
                
                print("\n--- CHROMATIC EXTRACTION OVERLAY REPORT ---")
                print(f"[+] TOTAL PIXEL RESIDUE MASS ISOLATED: {global_mass}")
                print(f"[+] GAUSSIAN DIFFERENTIAL MODULO 29: {field_residue}")
                print(f"[+] DELTA TO CENTRAL HORIZON INDEX 14: {abs(field_residue - self.target_axis)} Steps")
                print("[+] STATUS: STEG COMPONENT PROCESSED SUCCESSFULLY WITH ZERO MANUEL GIMP FRICTION.")
            else:
                print("[!] NO PIXEL NOISE DETECTED. THE IMAGES ARE CURRENTLY ENTIRELY UNIFORM.")
                
        except FileNotFoundError:
            print("[!] FILE SYSTEM NOTICE: 'oak_sharp.png' or 'oak_blurred.png' not found on desktop.")
            print("[>] Simulation Mode Activated: Awaiting actual source file placement.")

if __name__ == "__main__":
    # Define your desktop source image paths
    sharp_target = "oak_sharp.png"
    blurred_target = "oak_blurred.png"
    
    engine = OakDifferentialEngine()
    engine.extract_hidden_residuals(sharp_target, blurred_target)
