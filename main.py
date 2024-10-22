import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import PPAAnalyzer
import random
import math

ppa = PPAAnalyzer.PPAAnalyzer()
l = [math.sin(2 * x) for x in range(1, 101)]
print(l)
ppa.analyze(l)



