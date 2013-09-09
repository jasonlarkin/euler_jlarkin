import numpy as np
import scipy as sp

num1 = 3.0
num2 = 5.0

num_max = 10.0

num_div1 = np.floor(num_max/num1)
num_div2 = np.floor(num_max/num2)

print num_div1
print num_div2

print np.sum(num1*(np.arange(1,num_div1,1)))
print np.sum(num2*(np.arange(1,num_div2,1)))



