import math

class SignalGenerator:
    def __init__(self):
        pass
    def generate_sine(self, frequency: float, length: int) -> list:
        l = []
        phase = 0
        for i in range(0, length + 1):
            l.append(math.sin(phase))
            phase += (frequency / 48000) * 2 * math.pi

        return l