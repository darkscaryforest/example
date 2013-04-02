#!/usr/bin/python

print "1. Just printing a literal string"

testStr1 = "*This is a test string*"
print "2. Printing a string variable: " + testStr1 + " and its length: " 
print len(testStr1)

print "3. Concatenating that integer to this string: " + str( len(testStr1) )

print "4. Printing just the 2nd and 3rd characters: " + testStr1[1:3] + " and then the rest: " + testStr1[3:]

testStr2 = "*another string*"
testStr2 += testStr1
print "5. The concatenation of two string variables (possibly inefficient): " + testStr2

testStr1 = "  \twhitespace is before and after\n\n\n"
print "6. The strip function will take out all whitespace before and after a string:\n" \
	"BEFORE:" + testStr1 + "AFTER:" + testStr1.strip()

testStr2 = "one two three four"
print "7. We can search the string for a substring and get the index for where it starts.\n" \
	"Searching for three:\n" + str( testStr2.index("three") )

print "8. Combining that with the str length we can just print out what comes after three:\n" \
	+ testStr2[ testStr2.index("three") + len("three"):]
