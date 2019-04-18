#Purser, Charles N.
#cnp1474
#04-16-2019

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def applyShelvingFilter(inName, outName, g, fc) :
    #init
    x, fs = sf.read(inName)
    fftos = np.fft.fft(x) #fft of original signal
    ffto = np.fft.fftfreq(len(fftos), d=1/fs)
    N = len(fftos)
    thetac = ((2*np.pi*fc)/fs)
    mu = 10**(g/20)
    gamma = ((1-(4/(1+mu))*np.tan(thetac/2))/(1+(4/(1+mu))*np.tan(thetac/2)))
    alpha = ((1-gamma)/2)
    u = np.zeros(N)
    y = np.zeros(N)

    #filter
    n = 0
    u[n] = alpha*(x[n])
    n += 1
    while(n<N) : 
        u[n] = alpha*(x[n]+x[n-1]) + gamma*u[n-1]
        y[n] = x[n] + (mu-1)*u[n]
        n += 1

    fftfs = np.fft.fft(y)
    fftf = np.fft.fftfreq(len(fftfs), d=1/fs)
    ymax1 = max(abs(fftos))
    ymax2 = max(abs(fftfs))
    ymax = max(ymax1, ymax2)
    ymax += 100

    # plot
    f1 = plt.subplot(121)
    f1.set_title('original signal')
    f1.set_xlabel('Hz')
    f1.set_ylim([0, ymax])
    f1.plot(abs(ffto[:int(N/4)]), abs(fftos[:int(N/4)]))
    f2 = plt.subplot(122)
    f2.set_title('filtered signal')
    f2.set_xlabel('Hz')
    f2.set_ylim([0, ymax])
    f2.plot(abs(fftf[:int(N/4)]),abs(fftfs[:int(N/4)]))
    plt.show()

    #output WAV
    sf.write(outName, y, fs)


##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
