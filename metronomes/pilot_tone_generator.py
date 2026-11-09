#!/usr/bin/env python3
"""
Module: pilot_tone_generator.py
Description: Generates a pristine, zero-dependency 64 Hz acoustic pilot tone wave 
             file to serve as the structural temporal metronome clock.
"""
import wave
import struct
import math

def generate_64hz_pilot_tone(filename="pilot_tone_64hz.wav", duration_seconds=3.0):
    sample_rate = 44100  # Standard audio CD sampling rate
    frequency = 64.0     # The deterministic acoustic pilot tone frequency
    amplitude = 32767    # Max volume capacity for 16-bit audio integers
    
    num_samples = int(sample_rate * duration_seconds)
    
    print(f"[+] Opening audio stream context for: {filename}")
    wav_file = wave.open(filename, "w")
    # Channels: 1 (Mono), Sample Width: 2 bytes (16-bit), Framerate: 44100
    wav_file.setparams((1, 2, sample_rate, num_samples, "NONE", "not compressed"))
    
    print(f"[+] Synthesizing 64 Hz phase-locked acoustic wave-front...")
    for i in range(num_samples):
        # Calculate sine positioning along the spatial time axis
        t = float(i) / sample_rate
        value = int(amplitude * math.sin(2.0 * math.pi * frequency * t))
        # Pack the integer value into binary 16-bit LE PCM data bytes
        data = struct.pack("<h", value)
        wav_file.writeframesraw(data)
        
    wav_file.close()
    print(f"[=>] Pilot tone successfully rendered to disk.")

if __name__ == "__main__":
    generate_64hz_pilot_tone()
