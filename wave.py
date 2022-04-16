import numpy as np


class WaveTable:
    def __init__(self, rate, phase):
        self.samples = np.sin(2 * np.pi * np.arange(rate) / rate)
        self.phase = phase % len(self.samples)

    def next(self, chunk, frequency):
        # can't make fractional frequencies
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
        self.rate = rate

    def next(self, chunk, duration=1):
        data = np.arange(0)
        for i in range(int(self.rate // chunk * duration)):
            data = np.concatenate((data, self.wave_table.next(chunk, self.frequency)))
        # append the rest of the data to complete full seconds.
        # data = np.concatenate((data, self.wave_table.next(self.rate % chunk * duration)))
        return self.amplitude * data


