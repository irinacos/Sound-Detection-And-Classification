import numpy as np

def gabor_filter(size, sigma, freq):
    n = np.arange(size)
    mean = size / 2    # jumatatea ferestrei filtrului Gaussian
    g = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((n - mean) ** 2) / (2 * sigma ** 2))

    cos_h = g * np.cos(2 * np.pi * freq * n)
    sin_h = g * np.sin(2 * np.pi * freq * n)

    return cos_h, sin_h