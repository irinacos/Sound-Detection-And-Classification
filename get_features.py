import numpy as np
from filters_set import gabor_filters, M, size

K = size            # numar esantioane intr-o fereastra
n = K - 1           # indicele ultimei valori din filtru
t = 12 / 1000       # milisecunde

def get_features(audios, fs):
    delta = int(t * fs)  # numar esantioane intre ferestre
    filters = gabor_filters(K, fs, M)

    feat_train = []

    for a in audios:
        F = int((len(a) - K) // delta + 1)   # numarul de ferestre din semnal
        last_window_start = len(a) - K + 1

        windows = []        # lista de ferestre
        for window_start in range(0, last_window_start, delta):
            windows.append(a[window_start : window_start + K])

        # o(F, M) = w(F, K) * h(K, M)
        o = np.zeros((F, M))
        for f, window in enumerate(windows):
            for m, fil in enumerate(filters):
                h = fil[0]  # componenta cos a filtrului Gabor
                o[f, m] = sum(window[k] * h[n - k] for k in range(len(window)))

        o = np.abs(o)
        mean = np.mean(o, axis=0)   # media pe coloane -> (1, M)
        sigma = np.std(o, axis=0)   # deviatia std pe coloane -> (1, M)

        v = np.concatenate([mean, sigma])   # vector caracteristici pentru un semnal audio -> (1, 2M)
        feat_train.append(v)

    feat_train = np.array(feat_train)       # matrice caracteristici pentru toate semnalele -> (D, 2M)
    return feat_train