#Purser, Charles N.
#cnp1474
#04/23/2019

"""
    Wed Nov  7 10:16:17 CST 2018

    given two audio files, each of which consists of a mixture
    of two audio sources, perform blind source separation
"""


import numpy as np
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA, PCA


def unmixAudio(leftName, rightName) :
    audio1, fs1 = sf.read(leftName)
    audio2, fs2 = sf.read(rightName)
    matrix = np.c_[audio1, audio2]
    ica = FastICA(n_components=2)
    S_ = ica.fit_transform(matrix)
    S_ = S_*10
    sf.write("unmixed0.wav", S_[:,0], fs1)
    sf.write("unmixed1.wav", S_[:,1], fs2)

###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
