import numpy as np
import scipy
from matplotlib import pyplot as plt
from gabor_filter import gabor_filter

M = 12
size = 1102
data = scipy.io.loadmat('data.mat')
fs = data['fs'][0, 0]

def convert_mel(f):
    return 1127 * np.log(1 + f / 700)

def convert_norm(f_mel):
    return 700 * (np.exp(f_mel / 1127) - 1)

def gabor_filters(size, fs, M):
    freq_a = convert_mel(0)
    freq_b = convert_mel(fs / 2)
    seg_mel = np.linspace(freq_a, freq_b, M + 1)
    seg_norm = convert_norm(seg_mel)

    c = []  # centrele segmentelor pe scala normala
    for i in range(len(seg_norm) - 1):
        c.append((seg_norm[i] + seg_norm[i + 1]) / 2)

    l = []  # lungimile segmentelor pe scala normala
    for i in range(len(seg_norm) - 1):
        l.append(seg_norm[i + 1] - seg_norm[i])

    c = np.array(c)
    l = np.array(l)

    freq = c / fs
    sigma = fs / l

    filters = []
    for f, s in zip(freq, sigma):
        cos_h, sin_h = gabor_filter(size, s, f)
        filters.append((cos_h, sin_h))

    return filters


first_cos, first_sin = gabor_filters(size, fs, M)[0]

plt.figure()
plt.plot(first_cos)
plt.xlim(0, 1200)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-3, 3))
plt.title("Gabor filter - cos")
plt.savefig("id_gabor_cos.png")
plt.close()

plt.figure()
plt.plot(first_sin)
plt.xlim(0, 1200)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-3, 3))
plt.title("Gabor filter - sin")
plt.savefig("id_gabor_sin.png")
plt.close()