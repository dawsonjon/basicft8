# These imports tell python which modules to include. Numpy provides
# FFTs and convenient array manipulation. pyaudio provides access to
# sound cards.

import numpy
import scipy.signal
import pyaudio
import wave
import sys
import time
import re
import threading

from matplotlib import pyplot as plt


m = numpy.zeros((50, 50))

costas_matrix = numpy.zeros((8, 9))
costas_symbols = [ 2, 5, 6, 0, 4, 1, 3 ]
for i in range(0, len(costas_symbols)):
    costas_matrix[i][costas_symbols[i]] = 1
    m[i][costas_symbols[i]] = 1

strengths = scipy.signal.correlate2d(m, costas_matrix)

plt.figure()
plt.imshow(strengths)
plt.show()
