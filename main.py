import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import kbhit

import wave

# Script constants.
CHUNK = 1024
SRATE = 44100
FIGSIZE = (19.2, 10.8)

# Random seed.
np.random.seed(341)

# Matplotlib figure and axes.
fig, ax = plt.subplots(figsize=FIGSIZE)


'''

TODO

    import scyPi for wave shapes utils.
    
    Additive synthesis
    FM synthesis
    Subtractive synthesis
    Karplus-Strong
    
    Wave class
        attributes:
            WaveTable instance
            phase
            frequency
            amplitude
        methods:
            get a slice of the wave (in secs.)
    WaveTable
    
    - Piano keyboard (using wave-table) that generates (ADSR) a freq, and can, to user demand, generate its harmonics
      (chords).
        - ABC notation sheet player.
    - Same idea, single key. (noteOn/Off) Either main frequency as its mods can be modified (FM?).
    - H4E5? Polyphonic piano
    - Note drops (in pitch) after a delay
    
'''


def main():
    zeros = np.zeros(SRATE)
    random = np.random.uniform(1, -1, SRATE)
    one = wave.Wave(SRATE, 1, 0.8, 0)
    de_phased = wave.Wave(SRATE, 2, 0.3, SRATE//2)
    forty = wave.Wave(SRATE, 40, 0.5, 0)
    w = x = y = np.arange(0)
    for i in range(80):
        w = np.concatenate((w, one.next(CHUNK)))
        x = np.concatenate((x, de_phased.next(CHUNK)))
        y = np.concatenate((y, forty.next(CHUNK)))

    carrier = osc(67, 2.45, .8)
    modulator = osc(.65, 2.45, .35)
    result, modded = mod(carrier, modulator)

    plt.title('Modulated wave')
    ax.set(ylim=(-2, 2), yticks=np.arange(-2, 3, 1))
    ax.plot(w)
    ax.plot(x)
    ax.plot(y)

    plt.show()


def play():
    data = np.zeros(SRATE)
    kb = kbhit.KBHit()
    stream = sd.OutputStream(
        samplerate=SRATE,
        blocksize=CHUNK,
        channels=len(data.shape))

    frame = 0
    c = ''

    stream.start()
    print('Pulsa \'p\' para activar/desactivar o \'q\' para salir')
    while c != 'q':
        if kb.kbhit():
            c = kb.getch()

        stream.write(data)
        frame += CHUNK

    stream.stop()


def osc(freq, dur, vol):
    # Function that returns a wave of given frequency, duration (in secs, 1 sec = SRATE samples) and volume.
    return vol * np.sin(2 * np.pi * freq * np.arange(dur * SRATE) / SRATE)


def mod(carrier, modulator):
    modded = (modulator + .7) / 2
    return carrier * modded, modded


if __name__ == "__main__":
    main()
