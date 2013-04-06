#!/usr/bin/python

print "1. Here is a simple example of a while loop that breaks on the 4th iteration, but cuts the 3rd iteration short using continue"
a = 1
while a < 10:
        if(a == 3):
		a += 1
		continue;

	print "This is iteration number " + str(a)

	if(a == 4):
		break;
	a += 1

testStr1 = "*test string*"
print "2. Here is an if, else if, else statement with a string compare using string: " + testStr1
if(testStr1 == "*not a test string*"):
	print "I have no idea how this is printing"	
elif testStr1 == "*test string*":
	print "We matched the string!"
else:
	print "We didn't match the string somehow ERROR"

testListStr = ['first str', 'second str', 'third str', 'last str']
print "3. For statment iterates over on a list."

for test in testListStr:
	print "-" + test

print "4. For loop that iterates over a range, in this case it is up until the length of the testListStr array." \
	" Note: Not traditional C for loop syntax"
for i in range(len(testListStr)):
	print str(i) + " is " + testListStr[i]

a = 0
print "5. Statement that doesn't nothing: pass keyword"
if(a == 0):
	pass
