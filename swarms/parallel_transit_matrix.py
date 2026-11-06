import os

class ParallelTransitMatrix:
    def __init__(self):
        self.modulus = 29
        self.observer_axis = 14
        # Importing the core 12-house angular shift logic (30 degrees per house)
        self.house_degrees = 30 
        self.total_houses = 12

    def calculate_transit_skins(self, operational_mass):
        """
        Tracks how a dynamic text mass alters its internal skin across 12 parallel
        rotation points, using the logic of the cuneiform growth differentials.
        """
        print(r"--- INITIATING PARALLEL TRANSIT MATRIX: ALTERNATIVE ENTRANCE ---")
        print(f"[+] Ingested Base Payload Mass: {operational_mass}")
        
        house_deltas = {}
        
        # Track the text skin changes through each of the 12 spatial turnarounds
        for house in range(1, self.total_houses + 1):
            rotation_angle = house * self.house_degrees
            # Apply the dual crystallographic torque: mass interacting with rotational angle
            local_torque = operational_mass * rotation_angle
            residue = local_torque % self.modulus
            distance = abs(residue - self.observer_axis)
            
            house_deltas[house] = (residue, distance)
            print(f"[House {house:02d} | {rotation_angle:03d}° Rotation] -> Residue: {residue:02d} | Delta to Axis: {distance} Steps")
            
        return house_deltas

if __name__ == "__main__":
    matrix = ParallelTransitMatrix()
    # Using the current alternative entrance mass to initialize the parallel branch
    matrix.calculate_transit_skins(176902)
