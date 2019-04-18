# Purser, Charles N.
# cnp1474
# 2019-02-05

import sys
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

class hw02() : 
  
  notes = np.array([52, 52, 59, 59, 61, 61, 59, 59, 57, 57, 56, 56, 54, 54, 56, 52, 59, 59, 57, 57, 56, 56, 54, 54])
  y = []
  freq = []
  for i in notes : 
    freq.append( (440*(2**((i-49)/12))) )

  for i in freq :  
    for t in np.arange(0, 0.5, (1/8000)) :
      y.append( np.cos(2*np.pi*i*t))
  sf.write( 'twinkle.wav', y, 8000 )
