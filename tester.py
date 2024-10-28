import random
from copy import deepcopy

from lib import analyzer, signal_generator
from devices.dcx2496 import DCX2496

SAMPLERATE = 48000

ppa = analyzer.PPAAnalyzer()
sg = signal_generator.SignalGenerator()

sine = sg.generate_sine(5000, 10000)
test_signal = deepcopy(sine)


for i in range(0, len(test_signal)):
    test_signal[i] += (random.random()*2) - 1



#ppa.analyze(test_signal, SAMPLERATE)
d = DCX2496("1", b"\x01")
d.send_serial(b"\x20",b"\x01\x01\x02\x01\x52")


