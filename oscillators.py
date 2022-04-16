import numpy as np


SRATE = 44100


def osc(freq, dur, vol):
    # Function that returns a wave of given frequency, duration (in secs, 1 sec = SRATE samples) and volume.
    return vol * np.sin(2 * np.pi * freq * np.arange(dur * SRATE) / SRATE)


def mod(carrier, modulator):
    modded = (modulator + .7) / 2
    return carrier * modded, modded
