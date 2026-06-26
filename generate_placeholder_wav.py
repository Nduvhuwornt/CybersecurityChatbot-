#!/usr/bin/env python3
"""
Generates a minimal valid WAV file as a placeholder greeting.
Replace Resources/greeting.wav with your own recorded voice greeting.
Record yourself saying: "Hello! Welcome to the Cybersecurity Awareness Bot. I'm here to help you stay safe online."
"""
import struct
import os

def create_placeholder_wav(path: str):
    """Creates a short silent WAV file as a placeholder."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    sample_rate = 22050
    duration_seconds = 1
    num_samples = sample_rate * duration_seconds
    num_channels = 1
    bits_per_sample = 16
    byte_rate = sample_rate * num_channels * bits_per_sample // 8
    block_align = num_channels * bits_per_sample // 8
    data_size = num_samples * block_align

    with open(path, 'wb') as f:
        # RIFF header
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + data_size))
        f.write(b'WAVE')

        # fmt chunk
        f.write(b'fmt ')
        f.write(struct.pack('<I', 16))           # chunk size
        f.write(struct.pack('<H', 1))            # PCM format
        f.write(struct.pack('<H', num_channels))
        f.write(struct.pack('<I', sample_rate))
        f.write(struct.pack('<I', byte_rate))
        f.write(struct.pack('<H', block_align))
        f.write(struct.pack('<H', bits_per_sample))

        # data chunk (silence)
        f.write(b'data')
        f.write(struct.pack('<I', data_size))
        f.write(b'\x00' * data_size)

    print(f"Placeholder WAV created at: {path}")
    print("IMPORTANT: Replace this with a real voice recording!")

if __name__ == '__main__':
    create_placeholder_wav('CybersecurityChatbot/Resources/greeting.wav')
