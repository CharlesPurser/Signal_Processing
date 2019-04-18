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
    pass


###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
