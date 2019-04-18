#Purser, Charles N.
#cnp1474
#2019-02-26

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
from scipy import ndimage

class hw04_3() : 
  boat = img.imread("boat.512.tiff")
  clock = img.imread("clock-5.1.12.tiff")
  man = img.imread("man-5.3.01.tiff")
  tank = img.imread("tank-7.1.07.tiff")
  darin = img.imread("darinGrayNoise.jpg")
  
  data = np.array([boat, clock, man, tank])

  #lowpass filter
  lpf = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

  #highpass filter
  hpf = np.array([1, -1])

  #convolve filters with each image
  
  #display original boat image
  plt.title("Original Boat")
  plt.imshow(boat)
  plt.show()

  #blur boat image
  bboat = []
  for i in boat : 
    bboat.append(np.convolve(i, lpf))
  bboat = np.array(bboat)

  #display blurred boat image
  plt.title("Blurred Boat")
  plt.imshow(bboat)
  plt.show()

  #edge boat image
  eboat = []
  for i in boat : 
    eboat.append(np.convolve(i, hpf))
  eboat = np.array(eboat)

  #display edged boat image
  plt.title("Edged Boat")
  plt.imshow(eboat)
  plt.show()

  #display original clock image
  plt.title("Original Clock")
  plt.imshow(clock)
  plt.show()

  #blur clock image
  bclock = []
  for i in clock : 
    bclock.append(np.convolve(i, lpf))
  bclock = np.array(bclock)

  #display blurred clock image
  plt.title("Blurred Clock")
  plt.imshow(bclock)
  plt.show()

  #edge clock image
  eclock = []
  for i in clock : 
    eclock.append(np.convolve(i, hpf))
  eclock = np.array(eclock)

  #display edged clock image
  plt.title("Edged Clock")
  plt.imshow(eclock)
  plt.show()

  #display original man image
  plt.title("Original Man")
  plt.imshow(man)
  plt.show()

  #blur man image
  bman = []
  for i in man : 
    bman.append(np.convolve(i, lpf))
  bman = np.array(bman)

  #display blurred man image
  plt.title("Blurred Man")
  plt.imshow(bman)
  plt.show()

  #edge man image
  eman = []
  for i in man : 
    eman.append(np.convolve(i, hpf))
  eman = np.array(eman)

  #display edged man image
  plt.title("Edged Man")
  plt.imshow(eman)
  plt.show()

  #display tank image
  plt.title("Original Tank")
  plt.imshow(tank)
  plt.show()

  #blur tank image
  btank = []
  for i in tank : 
    btank.append(np.convolve(i, lpf))
  btank = np.array(btank)

  #display blurred tank image
  plt.title("Blurred Tank")
  plt.imshow(btank)
  plt.show()

  #edge tank image
  etank = []
  for i in tank : 
    etank.append(np.convolve(i, hpf))
  etank = np.array(etank)

  #display edged tank image
  plt.title("Edged Tank")
  plt.imshow(etank)
  plt.show()

  #display original darin image
  plt.title("Original Darin")
  plt.imshow(darin)
  plt.show()

  #convolve with a lowpass filter
  adarin = []
  for i in darin : 
    adarin.append(np.convolve(i,lpf))
  adarin = np.array(adarin)

  #display processed image
  plt.title("Averaged Darin")
  plt.imshow(adarin)
  plt.show()

  #apply median filter
  mdarin = ndimage.median_filter(darin, 5)

  #display processed image
  plt.title("Processed Darin")
  plt.imshow(mdarin)
  plt.show()