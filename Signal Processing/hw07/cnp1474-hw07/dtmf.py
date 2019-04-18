#Purser, Charles N.
#cnp1474
#04-08-2019

from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram


def processTones(name, L, fs, samplesPerTone) :
    
    #init
    signal = np.genfromtxt(name, delimiter= ',')
    freqs = [697, 772, 852, 941, 1209, 1336, 1477]
    phoneNumber = []
    hn = []

    #Bandpass filters
    for i in freqs : 
        temp = []
        for j in range(L) :
            temp.append( ((2/L)*(np.cos((2*np.pi*i*j)/fs))) )
        hn.append(temp)

    #Figure 1
    for i in hn : 
        x, y = freqz(i)
        plt.plot(((x*8000)/(2*np.pi)), abs(y))

    plt.xlabel('Hertz')
    plt.title('Frequency Responses of Bandpass Filters')
    plt.show()
    
    #Decode the signal
    for i in range(0,len(signal),4000) : 
        high = [] 

        for j in hn : 
            high.append(np.mean(np.convolve(signal[i:(i+4000)],j)**2))
        
        if(high[0] == max(high[:4])) :
            if(high[4] == max(high[4:])) : 
                phoneNumber.append('1')
            elif(high[5] == max(high[4:])) : 
                phoneNumber.append('2')
            else : 
                phoneNumber.append('3')
        elif(high[1] == max(high[:4])) : 
            if(high[4] == max(high[4:])) : 
                phoneNumber.append('4')
            elif(high[5] == max(high[4:])) : 
                phoneNumber.append('5')
            else : 
                phoneNumber.append('6')
        elif(high[2] == max(high[:4])) : 
            if(high[4] == max(high[4:])) : 
                phoneNumber.append('7')
            elif(high[5] == max(high[4:])) : 
                phoneNumber.append('8')
            else : 
                phoneNumber.append('9')
        else : 
            if(high[4] == max(high[4:])) : 
                phoneNumber.append('*')
            elif(high[5] == max(high[4:])) : 
                phoneNumber.append('0')
            else : 
                phoneNumber.append('#')      

    phoneNumber = ''.join(phoneNumber)

    #Figure 2
    f, t, Sxx = spectrogram(signal, fs)
    plt.pcolormesh(t, f, Sxx)
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')
    plt.show()

    return phoneNumber

#############  main  #############
if __name__ == "__main__":
    filename = "tones-7481414.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone, 
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)
    
    print(phoneNumber)
