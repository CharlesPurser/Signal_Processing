#Purser, Charles N.
#cnp1474
#04-01-2019

import numpy as np 
import soundfile as sf 
import matplotlib.pyplot as plt 

def processFile(fn, offset) :
    audio = sf.read(fn)
    signal = np.array(audio[0])
    fs = audio[1]
    
    #fft signal and find midpoint
    fftsig = np.fft.fft(signal)
    mid = (len(fftsig)/2)

    #plot before cleaning
    first = plt.subplot(211)
    first.plot(abs(fftsig))

    #clean the signal
    for i in range(int(mid-offset),int(mid+offset)) : 
        fftsig[i] = 0

    #plot cleaned values
    second = plt.subplot(212)
    second.plot(abs(fftsig))
    plt.show()

    #ifft and write
    cleansig = np.real(np.fft.ifft(fftsig))

    sf.write("cleanMusic.wav", cleansig, fs)


##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use

    processFile(filename, offset)


