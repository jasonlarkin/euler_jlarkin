import numpy as np
import fft_jl
import time
import sys
import matplotlib.pyplot as plt
from pylab import *

def main():
  sizes = [32,64,128,256,512,1024]
  times_dft = [];
  times_np_fft = []
  times_jl_fft = []
  for size in sizes:
    x = np.random.random(size)
    print '-'*40
    print 'The size is: ', size
    t0 = time.time()
    fft_jl.dft(x)
    t1 = time.time()
    print 'Time of fft_jl.dft: ', t1-t0
    times_dft.append(t1-t0)
    t0 = time.time()
    np.fft.fft(x)
    t1 = time.time()
    print 'Time of np.fft.fft: ', t1-t0
    times_np_fft.append(t1-t0)
    print 'Does dft match np.fft.fft? ', np.allclose(fft_jl.dft(x), np.fft.fft(x))
    t0 = time.time()
    fft_jl.fft(x)
    t1 = time.time()
    print 'Time of fft_jl.fft: ', t1-t0
    times_jl_fft.append(t1-t0)
    print 'Does fft match np.fft.fft? ', np.allclose(fft_jl.fft(x), np.fft.fft(x))
  
  f, axarr = plt.subplots(3, sharex=True)
  axarr[0].plot(sizes,times_dft)
  axarr[0].set_title('dft')
  axarr[1].plot(sizes,times_jl_fft)
  axarr[1].set_title('fft')
  axarr[2].plot(sizes,times_np_fft)
  axarr[2].set_title('np fft')
  plt.show()
    #sys.exit(0)
    #
    #%timeit fft_jl.dft(x)
    #print 'Time of np.fft.fft: '
    #%timeit np.fft.fft(x)

if __name__=='__main__':
  main()
