#http://stackoverflow.com/questions/2834652/seaching-for-an-element-in-a-circular-sorted-array
#
import sys
import os
import re

num = 10

array = [x for x in range(1,num,1)]
print array
num_cut = num/2
array_circ = []
array_circ.extend(array[-num_cut:])
print array_circ
array_circ.extend(array[:num_cut-1])
print array_circ
for num in array_circ:
  print num
