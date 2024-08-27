import numpy as np
import matplotlib.pyplot as plt
import pyaudio

p = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = 2048

# Minimal- und Maximalfrequenzen festlegen (in Hz)
MIN_FREQUENCY = 20
MAX_FREQUENCY = 20000

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                          frames_per_buffer=CHUNK_SIZE)


# Erstelle eine 1024 Sample lange Liste mit zufälligen Werten oder einem Testsignal
N = 2048  # Anzahl der Samples
t = np.linspace(0, 1, N)  # Zeitvektor

# Beispiel: Testsignal (Summe von zwei Sinuswellen)
f1 = 50  # Frequenz in Hz
f2 = 500  # Frequenz in Hz
signal = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t)
#signal = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.int16)

# Berechne die FFT
fft_result = np.fft.fft(signal)

# Frequenzachsenberechnung
frequencies = np.fft.fftfreq(N, d=(t[1] - t[0]))
#frequencies = np.linspace(MIN_FREQUENCY, MAX_FREQUENCY, N)
print(len(frequencies))

# Absolutwerte der FFT (Spektrale Amplitude)
fft_abs = np.abs(fft_result)
# Plot der FFT-Ergebnisse
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:N // 2], fft_abs[:N // 2])  # Nur positive Frequenzen anzeigen
plt.title('FFT des Signals')
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
