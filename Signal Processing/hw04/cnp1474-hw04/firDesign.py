#Purser, Charles N.
#cnp1474
#2019-02-25

import numpy as np 
import matplotlib.pyplot as plt

class hw04_2() : 

  #original signal
  data = np.genfromtxt('data-filtering.csv', delimiter= ',')
  plt.title("original signal")
  plt.plot(data)
  plt.show()

  #sampling rate
  fs = 2000

  #lowpass filter

  #cut-off freq
  fc = 50
  #normalized fc
  ft = fc/fs
  #filter length
  L = 21
  M = (L-1)
  wnl = []

  for i in np.arange(0, L) : 
    if(i == (M/2)) :
      wnl.append(2*ft)
    else : 
      wnl.append(np.sin(2*np.pi*ft*(i-(M/2)))/(np.pi*(i-(M/2))))

  #calculate 4hz signal
  
  #frequency
  freq = 4
  #time
  t = np.arange(0,1,1/fs)
  #angular freq
  ang = np.cos(2*np.pi*freq*t)
  
  #plot 4hz filter
  plt.title("4 Hz signal")
  plt.plot(ang)
  plt.show()
  
  fildata = np.convolve(data, wnl)

  #plot lowpass filtered data
  plt.title("application of lowpass filter")
  plt.plot(fildata)
  plt.show()

  #highpass filter
  plt.title("original signal")
  plt.plot(data[0:100])
  plt.show()

  #calculate 330hz signal
  
  #frequency
  freq = 330
  ang = np.cos(2*np.pi*freq*t)

  #plot 330hz filter
  plt.title("330hz signal")
  plt.plot(ang[0:100])
  plt.show()

  #cut-off freq
  fc = 280
  wnh = []
  ft = fc/fs

  for i in np.arange(0, L) : 
    if(i == (M/2)):
      wnh.append(1-(2*ft))
    else : 
      wnh.append(((-1)*np.sin(2*np.pi*ft*(i-(M/2)))/(np.pi*(i-(M/2)))))
  
  fildata = np.convolve(data, wnh)

  #plot highpass filtered data
  plt.title("application of highpass filter")
  plt.plot(fildata[0:100])
  plt.show()
