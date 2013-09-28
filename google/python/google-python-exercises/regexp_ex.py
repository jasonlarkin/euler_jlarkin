import sys
import os
import re

def last_char(str):
  return str[-1]

str_search = 'cunt lips nick.p@gmail.com shit fuck assy_biglips@shitstained.com'
str_regexp = r'([\w.]*)@([\w.]*)'

match = re.findall(str_regexp, str_search)
if match:
  print dict(match)['nick.p']

for user in match:
  print user

for idx, expr in enumerate(match):
  print idx, expr

#lists
list_ex = [1, '2', 'three', '4' + 'four']
print list_ex

# sets
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket), key=last_char):
  print f

