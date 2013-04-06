#!/usr/bin/python

class TestClass:
	varList = []
	varEx1 = 12
	def __init__(self):
		print "Special init function called."
		self.varEx2 = 13
		self.varEx3 = 14

	def funcEx(self):
		print self.varEx2
		return "hello world"

x = TestClass()
print "1. Classes, like functions, must be declared before use.\n" \
	"Calling a function in a class: " + x.funcEx() + "\n"\
	"Note that all functions take at least one argument..a reference to the instance object itself"
print "2. There's a huge difference between class and instance attributes.\n" \
	"class attributes are like static variables applied across all class instances\n" \
	"and instance variables are scoped to particular class instances.\n"
y = TestClass()
y.varList.append(5)
y.varEx1 = 2
y.varEx2 = 5
print "x's arributes after changes:\n" \
	"x.varList = " + str(x.varList) + "\n" \
	"x.varEx1 = " + str(x.varEx1) + "\n" \
	"x.varEx2 = " + str(x.varEx2) + "\n" \
	"x.varEx3 = " + str(x.varEx3)
print "y's arributes after changes:\n" \
	"y.varList = " + str(y.varList) + "\n" \
	"y.varEx1 = " + str(y.varEx1) + "\n" \
	"y.varEx2 = " + str(y.varEx2) + "\n" \
	"y.varEx3 = " + str(y.varEx3)
print "The list in both x and y is changed even though we updated\n" \
	"it through just y. Interestingly, the other int variable\n" \
	"varEx1 did not change in x.."
