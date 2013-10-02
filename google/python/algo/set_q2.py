#http://stackoverflow.com/questions/2834652/seaching-for-an-element-in-a-circular-sorted-array
#
import sys
import os
import re

#def enum(

def find_max(array):
  for idx, num in enumerate(array[2:]):
    print idx, array[idx+1]
    curr_diff = array[idx+1] - array_circ[idx]
    if curr_diff>=0:
      print array[idx+1]
  return

def binary_search(array,num):
  l = len(array)
#  sys.exit(0)
  mid = l/2
  if l==1 and array[mid]!=num:
    print "cannot find key"
  elif l==1 and array[mid]!=num:
    print "answer is ", array[mid] , num
  elif l==0:
    print "cannot find key"
  elif array[mid] == num:
    print "answer is: ", array[mid] , num
    return array[mid]
  else:
    if array[mid] > num:
      binary_search(array[:mid],num)
      print array[:mid]
    else:
      binary_search(array[mid:],num)
      print array[mid:]

def main():
  num = int(sys.argv[2])
  length = int(sys.argv[1])
  array = [x for x in range(1,length+1,1)]
  num_cut = length/2
  array_circ = []
  array_circ.extend(array[-num_cut:])
  array_circ.extend(array[:num_cut-1])
  #find_max(array_circ)
  print "input is: ", num, array
#  sys.exit(0)
  binary_search(array,num)
#  binary_search_circ(array_circ)
  return

if __name__ == '__main__':
  main()

