import numpy as np


class WaveTable:
    def __init__(self, rate, phase):
        self.samples = np.sin(2 * np.pi * np.arange(rate) / rate)
        self.phase = phase

    def next(self, chunk, frequency):
        data = np.zeros(chunk)
        for i in range(chunk):
            data[i] = self.samples[self.phase]
            self.phase = (self.phase + frequency) % len(self.samples)
        return data


class Wave:
    def __init__(self, rate, frequency, amplitude, phase):
        self.wave_table = WaveTable(rate, phase)
        self.frequency = frequency
        self.amplitude = amplitude
        # self.phase = phase

    def next(self, chunk, duration=1):
        data = np.arange(0)
        for i in range(duration):
            data = np.concatenate((data, self.wave_table.next(chunk, self.frequency)))
        return self.amplitude * data

