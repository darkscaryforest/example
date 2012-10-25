#!/usr/bin/python

def main():
  print "1. Functions in python have to be declared before use, and there is no prototyping.\n" \
        "Trick to make it look nice: declare main function first, followed by all functions, and then call main()"
  print "2. Above printing was example test function call giving 2 arguments.  Return code is " + str( testFunc("test1", "test2") )

def testFunc(arg1, arg2):
  print "\nArgument 1 is " + arg1 + " and argument 2 is " + arg2
  return 5

main()
