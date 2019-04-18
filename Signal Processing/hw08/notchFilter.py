#Purser, Charles N.
#cnp1474
#04-16-2019

import numpy as np
import matplotlib.pyplot as plt

def applyNotch(fs, dataFile) :
    #init
    x = np.genfromtxt(dataFile, delimiter= ',')
    N = len(x)
    y = np.zeros(N+100)
    f = 17  #freq is 17Hz  
    w = ((2*np.pi*f)/fs)   
    
    #calculate difference equation
    n = 0
    y[n] = x[n]
    n += 1
    y[n] = (1.8744*np.cos(w)*y[n-1])+x[n]-(2*np.cos(w)*x[n-1])
    n += 1   

    while(n < (N+100)) :
        if(n == (N-1)) :
            y[n] = (1.8744*np.cos(w)*y[n-1])-(0.8783*y[n-2])-(2*np.cos(w)*x[n-1])+x[n-2]
            n += 1
        elif(n == N) :
            y[n] = (1.8744*np.cos(w)*y[n-1])-(0.8783*y[n-2])+x[n-2]
            n += 1
        elif( n>N ) : 
            y[n] = (1.8744*np.cos(w)*y[n-1])-(0.8783*y[n-2])
            n += 1
        else :
            y[n] = (1.8744*np.cos(w)*y[n-1])-(0.8783*y[n-2])+x[n]-(2*np.cos(w)*x[n-1])+x[n-2]
            n += 1

    #plot 
    plt.title('Original Signal X')
    plt.xlim([-25, 625])
    plt.plot(x)
    plt.show()    
    plt.title('Filtered Signal Y')
    plt.ylim([-2.25, 2.25])
    plt.plot(y)
    plt.show()

    #Combine 10Hz and 33Hz signal
    t = np.arange(0, 1, 1/fs)
    f10 = np.cos(2*np.pi*10*t)
    f33 = np.cos(2*np.pi*33*t)
    fcom = np.convolve(f10, f33)
    
    #plot
    plt.title('Combined 10Hz and 33Hz Signal')
    plt.xlim([-25, 625])
    plt.plot(fcom)
    plt.show()


############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
