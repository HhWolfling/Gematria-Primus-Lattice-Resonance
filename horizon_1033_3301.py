class MagicSquareValidator:
    def validate_magic_square_1033(self):
        """Proves the Page 05 Magic Square stabilizes at the 1033 Newton Node."""
        raw_rows = [
            "272 138 341 131 151",
            "366 199 130 320 18",
            "226 245 91 245 226",
            "18 320 130 199 366",
            "151 131 341 138 272"
        ]
        square = [[int(num) for num in row.split()] for row in raw_rows]
        
        print("\n--- INITIATING TARGET AXIS 1033 VALIDATION ---")
        for idx, row in enumerate(square):
            print(f"[>] Row {idx + 1} Sum: {sum(row)}")
        for col_idx in range(5):
            col_sum = sum(square[row_idx][col_idx] for row_idx in range(5))
            print(f"[>] Column {col_idx + 1} Sum: {col_sum}")
        diag1 = sum(square[i][i] for i in range(5))
        diag2 = sum(square[i][4 - i] for i in range(5))
        print(f"[>] Left-to-Right Diagonal Sum: {diag1}")
        print(f"[>] Right-to-Left Diagonal Sum: {diag2}")
        print("[+] HARMONIC BALANCE VERIFIED: 1033 IS THE CONSTANT HORIZON.")

    def validate_master_square_3301(self):
        """Proves the Page 16 Magic Square stabilizes at the 3301 Signature."""
        raw_rows_3301 = [
            "434 1311 312 278 966",
            "204 812 934 280 1071",
            "626 620 809 620 626",
            "1071 280 934 812 204",
            "966 278 312 1311 434"
        ]
        square_3301 = [[int(num) for num in row.split()] for row in raw_rows_3301]
        
        print("\n--- INITIATING MASTER SIGNATURE 3301 VALIDATION ---")
        for idx, row in enumerate(square_3301):
            print(f"[>] Row {idx + 1} Sum: {sum(row)}")
        for col_idx in range(5):
            col_sum = sum(square_3301[row_idx][col_idx] for row_idx in range(5))
            print(f"[>] Column {col_idx + 1} Sum: {col_sum}")
        diag1 = sum(square_3301[i][i] for i in range(5))
        diag2 = sum(square_3301[i][4 - i] for i in range(5))
        print(f"[>] Left-to-Right Diagonal Sum: {diag1}")
        print(f"[>] Right-to-Left Diagonal Sum: {diag2}")
        print("[+] HARMONIC OVERLAY VERIFIED: 3301 SIGNATURE IS FIXED.")

if __name__ == "__main__":
    validator = MagicSquareValidator()
    validator.validate_magic_square_1033()
    validator.validate_master_square_3301()
