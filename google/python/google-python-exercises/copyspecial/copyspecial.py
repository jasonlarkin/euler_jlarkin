#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dirs,todir):
  for dir in dirs:
    filenames = os.listdir(os.path.abspath(dir))
    for file in filenames:
      match = re.search(r'__\w+__',file)
      if match:
        dir_abs = os.path.abspath(os.path.join(dir, file))
        if todir:
          todir_abs = os.path.join(todir,file)
          print dir_abs, todir_abs
          shutil.copy(dir_abs,todir)
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  dirs = args[2:]
  if args[0] == '--todir':
    todir = args[1]
    dirs = args[2]
    print args[:]
    get_special_paths(dirs,todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  get_special_paths(dirs,'')
  
if __name__ == "__main__":
  main()
