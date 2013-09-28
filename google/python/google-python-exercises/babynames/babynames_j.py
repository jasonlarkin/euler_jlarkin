import os
import sys
import re
from pylab import *
from subprocess import call

def get_names(line):
 # print line
  #match_tag = re.findall(r'<td>\w*</td>',line)
  #if match_tag:
    #rank = re.findall(r'\d*',match_tag[0])
    #nameboy = re.findall(r'\w*',match_tag[1])
    #namegirl = re.findall(r'\w*',match_tag[2])
    #print rank[4], nameboy[3], namegirl[3]
  match_tag = re.search(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',line)
  if match_tag:
    #print match_tag.group()
    match_name = re.findall(r'>(\w+)<',match_tag.group())
    return match_name[0] + ' ' + match_name[1] + ' ' + match_name[2]

def extract_names(filename,writeout):
  get_year(filename)
  f = open(filename, 'rU')
  fw = open(filename + '.ioutput','w')
  for line in f:
   # get_rank(line)
    names = get_names(line)
    if names:
      print names
      if writeout == '--writeout':
        fw.write(names + '\n')
  return

def get_rank(line):
  match_tag = re.search(r'<td>\d*</td>',line)
  if match_tag:
    #print match_tag.group()
    match_num = re.findall(r'\d*',match_tag.group())
    if match_num:
      print match_num[4]
      return match_num[4]

def get_year(filename):
  try:
    f = open(filename, 'rU')
    for line in f:
      match = re.search(r'Popularity in \d\d\d\d', line)
      if match:
        #print match.group()
        match_year = re.search(r'\d\d\d\d', match.group())
        if match_year:
          print match_year.group()
    return match_year.group()
  except IOError:
    sys.stderr.write('problem reading:' + filename)

def main():
  print 'in main'
  years_int = [num for num in range(1990,2008,2)]
  print years_int
  years = [str(year) for year in years_int]
  print years

  #if len(sys.argv)>3:
  #  print 'use: babynames_j.py filename --writeout'
  #else:  
  writeout = sys.argv[1]
  for filename in sys.argv[2:]:
    extract_names(filename,writeout)
  print sys.argv[:]

  return_code = call(["ls","-l"])
  return_code = call("grep 'Charlotte' *.ioutput", shell=True)
  print return_code
  return_code = call("grep 'Fiona' *.ioutput", shell=True)
  print return_code
  print os.path.abspath(filename)
  return


#boiler
if __name__ == '__main__':
  main()
