#Purser, Charles 
#cnp1474
#2019-03-24

import numpy as np
import matplotlib.pyplot as plt 

class hw04() : 
  
  #original signal
  fs = 2000
  data = np.genfromtxt('data-filtering.csv', delimiter= ',')

  #4 Hz signal
  t = np.arange(0,1,1/fs)
  fourhz = np.cos(2*np.pi*4*t)

  #lowpass filter
  lowpass = []
  fc = 50
  L = 21
  M = L-1
  ft = fc/fs

  for i in np.arange(0,L) : 
    if(i == (M/2)) :
      lowpass.append(2*ft)
    else : 
      lowpass.append(np.sin((2*np.pi*ft*(i-(M/2))))/(np.pi*(i-(M/2))))
  
  #lowpass signal

  lowpassconvolve = np.convolve(data, lowpass)


  first = plt.subplot(311)
  first.set_title('original signal')
  first.plot(data)
  second = plt.subplot(312)
  second.set_title('4 Hz signal')
  second.plot(fourhz)
  third = plt.subplot(313)
  third.set_title('application of lowpass filter')
  third.plot(lowpassconvolve)
  plt.tight_layout()
  plt.show()

  #330 Hz signal
  threehz = np.cos(2*np.pi*330*t)

  #highpass signal
  highpass = []
  fc = 280
  fs = 2000
  L = 21
  M = L-1
  ft = fc/fs 
  for i in np.arange(0,L) : 
    if(i == (M/2)) :
      highpass.append(1-(2*ft))
    else :
      highpass.append(-((np.sin(2*np.pi*ft*(i-(M/2))))/(np.pi*(i-(M/2)))))

  highpassconvolve = np.convolve(data, highpass)

  first = plt.subplot(311)
  first.set_title('original signal')
  first.plot(data[0:100])
  second = plt.subplot(312)
  second.set_title('330 Hz signal')
  second.plot(threehz[0:100])
  third = plt.subplot(313)
  third.set_title('application of highpass filter')
  third.plot(highpassconvolve[0:100])

  plt.tight_layout()
  plt.show()