import matplotlib.pyplot as plt
import numpy as np


class PPAAnalyzer:
    def __init__(self):
        pass

    def analyze(self, buffer: list, sample_rate: float):
        signal_arr = np.array(buffer, dtype=np.float64)

        fft_result = np.fft.fft(signal_arr)
        fft_abs = np.abs(fft_result)
        frequencies = np.fft.fftfreq(len(buffer), d=1/sample_rate)
        print(len(frequencies))

        plt.figure(figsize=(12, 6))
        plt.plot(frequencies[:len(buffer) // 2], 20 * np.log(fft_abs[:len(buffer) // 2]/fft_abs.max()))
        plt.title('FFT des Signals')
        plt.xlabel('Frequenz (Hz)')
        plt.ylabel('Amplitude (dB)')
        plt.grid(True)
        plt.show()