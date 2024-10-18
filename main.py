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

print("----------------------record device list---------------------")
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

print("-------------------------------------------------------------")

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, input_device_index=4,
                frames_per_buffer=CHUNK_SIZE)

N = 2048  # Anzahl der Samples
t = np.linspace(0, 1, N)
signal = []
for i in range(0, 10):
    signal.append(stream.read(CHUNK_SIZE))

signal_arr = np.array(signal, dtype=np.int16)
print(type(signal_arr))
# Berechne die FFT
fft_result = np.fft.fft(signal_arr)

# Frequenzachsenberechnung
frequencies = np.fft.fftfreq(2048*10, d=(t[1] - t[0]))
#frequencies = np.linspace(MIN_FREQUENCY, MAX_FREQUENCY, N)
print(len(frequencies))

# Absolutwerte der FFT (Spektrale Amplitude)
fft_abs = np.abs(fft_result)
# Plot der FFT-Ergebnisse
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:2048*10 // 2], fft_abs[:2048*10 // 2])  # Nur positive Frequenzen anzeigen
plt.title('FFT des Signals')
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
