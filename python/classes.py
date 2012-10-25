#!/usr/bin/python

class TestClass:
  varEx = 12
  varEx2 = 0

  def __init__(self):
    print "Special init function called."

  def funcEx(self):
    print self.varEx
    return "hello world"

x = TestClass()
print "1. Classes, like functions, must be declared before use.\n" \
      "Calling a function in a class: " + x.funcEx() + \
      "Note that all functions take at least one argument..a reference to the instance object itself"

