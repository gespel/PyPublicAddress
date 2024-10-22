import random
from copy import deepcopy

import analyzer
import signal_generator

SAMPLERATE = 48000

ppa = analyzer.PPAAnalyzer()
sg = signal_generator.SignalGenerator()

sine = sg.generate_sine(5000, 10000)
test_signal = deepcopy(sine)


for i in range(0, len(test_signal)):
    test_signal[i] += (random.random()*2) - 1



ppa.analyze(test_signal, SAMPLERATE)



