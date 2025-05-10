# main.py
from config import *
from transmitter import generate_bits, modulate
from channel import awgn, scintillation
from receiver import demodulate, calculate_ber
import matplotlib.pyplot as plt

bits = generate_bits(N_BITS)
tx_signal = modulate(bits, MODULATION)
ber_list = []

for snr_db in SNR_RANGE_DB:
    if NOISE_MODEL == 'AWGN':
        rx_signal = awgn(tx_signal, snr_db)
    elif NOISE_MODEL == 'Scintillation':
        rx_signal = scintillation(tx_signal)
    rx_bits = demodulate(rx_signal)
    ber = calculate_ber(bits, rx_bits)
    ber_list.append(ber)

# Plot
plt.semilogy(SNR_RANGE_DB, ber_list, 'o-')
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title(f"{MODULATION} over {NOISE_MODEL}")
plt.grid(True)
plt.show()
