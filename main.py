import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
# import sciPy for wave shapes utils.

import kbhit
import wave
import oscillators

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
    
    Additive synthesis
    FM synthesis
    Subtractive synthesis
    Karplus-Strong
    
    - ABC notation sheet player.
    - Piano keyboard (using wave-table)
        
    - Same idea, single key. (noteOn/Off) Either main frequency as its mods can be modified (FM?).
    - H4E5? Polyphonic piano
    
    - Note drops (in pitch) after a delay
    - Generate harmonics to a note
    
'''


def main():
    zeros = np.zeros(SRATE)
    random = np.random.uniform(1, -1, SRATE)
    one = wave.Wave(SRATE, 1, .8, 0)
    de_phased = wave.Wave(SRATE, 1, 0.8, SRATE//2)
    forty = wave.Wave(SRATE, 40, .35, 0)
    w = x = y = np.arange(0)
    w = np.concatenate((w, one.next(CHUNK)))

    carrier = oscillators.osc(1.5, 1, .8)
    modulator = oscillators.osc(.65, 1, .35)

    plt.title('Modulated wave')
    ax.set(ylim=(-2, 2), yticks=np.arange(-2, 3, 1))
    ax.plot(w)
    ax.plot(carrier)
    ax.plot(modulator)

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


if __name__ == "__main__":
    main()
