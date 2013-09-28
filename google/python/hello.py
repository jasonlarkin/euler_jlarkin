#!/usr/bin/python

import sys

def main():
  print 'Hello there', sys.argv[1]

if __name__=='__main__':
	main()

#The outermost statements in a Python file, or "module", do its one-time setup -- those statements run from top to bottom the first time the module is imported somewhere, setting up its variables and functions. A Python module can be run directly -- as above "python hello.py Bob" -- or it can be imported and used by some other module. When a Python file is run directly, the special variable "__name__" is set to "__main__". Therefore, it's common to have the boilerplate if __name__ ==... shown above to call a main() function when the module is run directly, but not when the module is imported by some other module.

