import os.path
import uuid
import logging
import matplotlib.pyplot as plt
import numpy as np


class PPAAnalyzer:
    def __init__(self, render_folder: str = "renders"):
        logging.basicConfig(level=logging.INFO)
        logging.info('Starting PPAAnalyzer...')
        if not os.path.isdir(render_folder):
            os.mkdir(render_folder)
            self.render_folder = render_folder

    def render_fft(self, buffer: list, sample_rate: float) -> str:
        logging.info("Analyzing...")
        signal_arr = np.array(buffer, dtype=np.float64)

        fft_result = np.fft.fft(signal_arr)
        fft_abs = np.abs(fft_result)
        frequencies = np.fft.fftfreq(len(buffer), d=1/sample_rate)
        #print(len(frequencies))

        plt.figure(figsize=(12, 6))
        plt.plot(frequencies[:len(buffer) // 2], 20 * np.log(fft_abs[:len(buffer) // 2]/fft_abs.max()))
        plt.title('FFT des Signals')
        plt.xlabel('Frequenz (Hz)')
        plt.ylabel('Amplitude (dB)')
        plt.grid(True)
        filename = os.path.join(self.render_folder, str(uuid.uuid4()) + ".png")
        plt.savefig(filename)
        logging.info('Saved analysis results to {}'.format(filename))
        return filename