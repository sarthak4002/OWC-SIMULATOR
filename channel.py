# channel.py
import numpy as np

def awgn(signal, snr_db):
    snr = 10 ** (snr_db / 10)
    noise_std = 1 / np.sqrt(2 * snr)
    noise = np.random.normal(0, noise_std, len(signal))
    return signal + noise

def scintillation(signal, alpha=1.5, beta=2.0):
    gamma_noise = np.random.gamma(alpha, beta, size=len(signal))
    return signal * gamma_noise
