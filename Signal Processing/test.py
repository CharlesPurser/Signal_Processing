import numpy as np 

class test() :
    x1 = [1,2,1,2]
    x1f = np.fft.fft(x1)
    x2 = [3,0,-1,-4]
    x2f = np.fft.fft(x2)
    xn = [4,2,0,-2]
    xnf = np.fft.fft(xn)
    x12 = np.convolve(x1, x2)
    xk = [-12,0,-12,0]
    xkif = np.fft.ifft(xk)
    xz1 = [1,2,1,2,0,0,0]
    xz1f = np.fft.fft(xz1)
    xz2 = [3,0,-1,-4,0,0,0]
    xz2f = np.fft.fft(xz2)
    xzk = np.multiply(xz1f, xz2f)
    xzkif = np.fft.ifft(xzk)
    print(xzkif)
