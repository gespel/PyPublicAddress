import numpy as np
import matplotlib.pyplot as plt

class PPAAnalyzer:
    def __init__(self):
        pass

    def analyze(self, buffer: list):
        t = np.linspace(0, 1, len(buffer))
        signal_arr = np.array(buffer, dtype=np.float64)
        print(signal_arr)

        fft_result = np.fft.fft(signal_arr)

        # Frequenzachsenberechnung
        frequencies = np.fft.fftfreq(len(buffer), d=(t[1] - t[0]))
        # frequencies = np.linspace(MIN_FREQUENCY, MAX_FREQUENCY, N)
        print(len(frequencies))
        # Absolutwerte der FFT (Spektrale Amplitude)
        fft_abs = np.abs(fft_result)
        # Plot der FFT-Ergebnisse
        plt.figure(figsize=(12, 6))
        plt.plot(frequencies[:len(buffer) // 2], fft_abs[:len(buffer) // 2])  # Nur positive Frequenzen anzeigen
        plt.title('FFT des Signals')
        plt.xlabel('Frequenz (Hz)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()