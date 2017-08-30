#!/usr/bin/python

def main():
  print "1. Functions in python have to be declared before use, and there is no prototyping.\n" \
        "Trick to make it look nice: declare main function first, followed by all functions, and then call main()"
  print "2. Above printing was example test function call giving 2 arguments.  Return code is " + str( testFunc("test1", "test2") )
  print "3. kwargs"
  testFunc2(test = "test arg 1", other = "test arg 2")
  print "3. kwargs with default arg"
  testFunc3(test = "test arg 1", test2 = "test arg 2", other = "apple")
  print "3. kwargs with default arg missing"
  testFunc3(test = "test arg 1", test2 = "test arg 2")
  #testFunc2("test arg 1", "test arg 2") doesn't work! needs keywords for each arg
  print "4. args"
  testFunc4("test1", "test2")

def testFunc(arg1, arg2):
  print "\nArgument 1 is " + arg1 + " and argument 2 is " + arg2
  return 5

def testFunc2(**kwargs):
    for k in kwargs.keys():
        print("%s = %s" % (k, kwargs[k]))

def testFunc3(other = "banana", **kwargs):
    print("other = %s" % other)
    for k in kwargs.keys():
        print("%s = %s" % (k, kwargs[k]))

def testFunc4(*args):
    for i in args:
        print("%s" % (i))

main()
