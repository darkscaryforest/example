#!/usr/bin/python

import sys

argsLen = len(sys.argv)
if(argsLen < 3):
	print "Help: You didn't give any command line args. Provide two or more arguments to see full print out of example."
	exit(1)

print "1. One way to get commandline args is using sys. The first arg is always the program name: " + sys.argv[0]

print "2. The number of args given (including program name) is: " + str(argsLen)
