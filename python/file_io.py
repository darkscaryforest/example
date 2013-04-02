#!/bin/python
import os, time

FILENAME = "file_io.txt"

# Open file for reading, -1 says to use operating
# system buffering size
newFile = open(FILENAME, "r", -1);

testnum = 0
str = newFile.read(20)

print "1. Reading 20 bytes from " + FILENAME + ":\n" + str

print "2. Putting the rest of entire file in a list delimited by newlines:"
strlist = newFile.readlines()
print strlist

newFile.close()

print "3. Getting the file creation time (nicely formatted) of " + FILENAME + ":"
print "%s" % time.ctime(os.path.getctime(FILENAME))

print "4. Getting file creation (last metadata change) using stat (unix time):"
statinfo = os.stat(FILENAME);
print statinfo.st_ctime
