# transmitter.py
import numpy as np

def generate_bits(N):
    return np.random.randint(0, 2, N)

def modulate(bits, scheme='OOK'):
    if scheme == 'OOK':
        return bits.astype(float)
    raise ValueError(f"Modulation {scheme} not implemented.")
