#http://stackoverflow.com/questions/11112789/merge-sort-implementation-check
import os
import re
import sys
import random
import timeit

def merge_sort(li):
  if len(li) < 2: return li
  m = len(li) / 2 
  return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
  print 'left array: ', l
  print 'right array: ', r
  result = []
  i = j = 0
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      result.append(l[i])
      i += 1
      print 'l[i] < r[j]', result
    else:
      result.append(r[j])
      j += 1 
      print 'l[i] > r[j]', result
  result += l[i:]
  print '+= l[i:]', result
  result+= r[j:]
  print '+=r[j:]',  result
#  sys.exit(0)
  return result

def main():
  random.seed('11111')
  list = [random.randint(0,1000) for x in xrange(int(sys.argv[1]))]
  print 'input is: ', list
  print merge_sort(list)  


if __name__=='__main__':
  main()
