#!/usr/bin/python

print "1. Just printing a literal string"

testStr1 = "*This is a test string*"
print "2. Printing a string variable: " + testStr1 + " and its length: " 
print len(testStr1)

print "3. Concatenating that integer to this string: " + str( len(testStr1) )

print "4. Printing just the 2nd and 3rd characters: " + testStr1[1:2] + " and then the rest: " + testStr1[3:]

testStr2 = "*another string*"
testStr2 += testStr1
print "5. The concatenation of two string variables (possibly inefficient): " + testStr2
