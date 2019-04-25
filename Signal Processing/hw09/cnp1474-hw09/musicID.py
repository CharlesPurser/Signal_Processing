#Purser, Charles N.
#cnp1474
#04/23/2019

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob

def classifyMusic() :
    files = glob.glob('song-*.wav')

    #init
    filename = []
    sig = []
    corsig = []
    onenorm = []

    #calculate signatures
    for i in files :
        filename.append(i)
        audio, fs = sf.read(i)
        f, t, Sxx = spectrogram(audio, fs=fs, nperseg=fs//2)
        sigtem = []
        for j in Sxx.T :
            temp = float("-inf")  
            count = 0
            index = 0
            for k in j : 
                if(k > temp) : 
                    temp = k
                    index = count
                count += 1
            sigtem.append(f[index])
        sig.append(sigtem)

    #calculate corrupt signature
    testaud, testfs = sf.read("testSong.wav")
    f, t, Sxx = spectrogram(testaud, fs=testfs, nperseg=testfs//2)
    for j in Sxx.T :
        temp = float("-inf")  
        count = 0
        index = 0
        for k in j : 
            if(k > temp) : 
                temp = k
                index = count
            count += 1
        corsig.append(f[index])    

    #one norm test
    for i in sig :     
        onenorm.append(sum(abs(np.subtract(i,corsig))))

    #sort lists
    n = len(onenorm)
    for i in range(n) : 
        for j in range(0, n-i-1) : 
            if(onenorm[j] > onenorm[j+1]) : 
                onenorm[j], onenorm[j+1] = onenorm[j+1], onenorm[j]
                filename[j], filename[j+1] = filename[j+1], filename[j]
    
    #print
    for i in range(5) :
        print(onenorm[i], "  ", filename[i])

    #plots
    plt.specgram(testaud, Fs=testfs)
    plt.show()
    for i in range(2) :
        x, fs = sf.read(filename[i])
        plt.specgram(x, Fs=fs)
        plt.show()

###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
