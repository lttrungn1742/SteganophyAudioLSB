# inFile = open('audio.wav','rb').read()

# count = 8

# a, b = (count -1) * 4, count * 4
# print(inFile[a:b])


# #outFile = open('outFile.wav','wb').write(inFile)

import wave
import contextlib
fname = 'audio.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)