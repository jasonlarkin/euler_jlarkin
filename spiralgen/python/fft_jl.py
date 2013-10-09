import numpy as np

def dft(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def fft(x):
  x = np.asarray(x, dtype=float)
  N = x.shape[0]

  if N % 2 > 0:
    raise ValueError("size of x must be a power of 2")
  elif N <= 32:
    return dft(x)
  else:
    x_even = fft(x[::2])
    x_odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([x_even + factor[:N / 2] * x_odd, x_even + factor[N / 2:] * x_odd])
