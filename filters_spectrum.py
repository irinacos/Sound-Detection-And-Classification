import numpy as np
import matplotlib.pyplot as plt
import scipy
from filters_set import size, fs, M, gabor_filters


def gabor_spectrum(filters, size):
    plt.figure()
    plt.xlim(0, 600)

    # spectru frecvente pozitive
    freqs = np.arange(size)[:size // 2]

    for (cos_h, sin_h) in filters:
        coefs = scipy.fft.fft(cos_h)
        magnitude = np.abs(coefs[:size // 2])
        plt.plot(freqs, magnitude)

    plt.title("Gabor Filters")
    plt.savefig("id_spectru_filtre.png")
    plt.close()

filters = gabor_filters(size, fs, M)
gabor_spectrum(filters, size)