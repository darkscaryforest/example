#!/usr/bin/python

num = 5
numstr = "10"
print "1. We have a number in a string here: " + numstr + ",\nyet it can be " \
	"easily converted to an int to add to another number. " \

anothernum = int(numstr) + num
# You can't directly concantenate ints and strings
print anothernum

print "2. It's easy to then convert that number back to a str: " + str(anothernum)

pi = 3.14159
print "3. It's also easy to convert a float to an int and vice versa:"
print int(pi)
print float(num)
