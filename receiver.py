# receiver.py
import numpy as np

def demodulate(rx_signal, threshold=0.5):
    return (rx_signal > threshold).astype(int)

def calculate_ber(tx_bits, rx_bits):
    return np.mean(tx_bits != rx_bits)
