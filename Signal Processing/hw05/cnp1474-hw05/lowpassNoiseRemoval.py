#Purser, Charles N.
#cnp1474
#2019-03-06

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import soundfile as sf

class hw05() : 

  audio = sf.read("P_9_2.wav")
  signal = np.array(audio[0])

  #sampling rate
  fs = audio[1]

  #lowpass filter

  #cut-off freq
  fc = 7500
  #normalized fc
  ft = fc/fs
  #filter length
  L = 101
  M = (L-1)
  hn = []
  #lowpass filter
  for i in range(0, L) : 
    if(i == (M/2)) :
      hn.append(2*ft)
    else : 
      hn.append(np.sin(2*np.pi*ft*(i-(M/2)))/(np.pi*(i-(M/2))))

  #plot freq response
  x, y = freqz(hn)
  plt.title("Frequency Response")
  plt.plot(x, abs(y))

  #hamming window
  wn = []
  for i in range(0, L) :
      wn.append((0.54-(0.46*np.cos((2*np.pi*i)/M))))

  #element wise multiplication
  hwn = []
  hwn = np.multiply(wn,hn)

  x, y = freqz(hwn)
  plt.plot(x, abs(y))
  plt.show()

  fixed = np.convolve(signal, hwn)

  sf.write('cleanMusic.wav', fixed, fs)
