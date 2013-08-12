#!/bin/python
import os, time, sys, getopt, encodings

PROG_NAME = sys.argv[0]
HELP = "Usage: " + PROG_NAME + " -k keyvalue [-i filename1] [-o filename2] [-h]\n" \
	"\t-i, --infile filename ; input file with string, otherwise will take from stdin\n" \
	"\t-o, --outfile filename ; output file to put xored input string, otherwise will print to stdout\n" \
	"\t-k, --key ; key to xor input string with (in decimal or hex. prefix with 0x for hex)\n" \
	"\t-f, --format ; output format: ascii (default), hex string, c style hex literal\n" \
	"\t-h, --help ; print this help message\n"
FILENAME = "file_io.txt"
KEY = 0x00
KEY_SIZE = 0x00
TEXT1="This is some example text"
TEXT2="A}|f5|f5fzxp5pmtxeyp5apma"
result = ""
argsLen = len(sys.argv)

def formatText(inputStr, form):
	if(form == "ascii"):
		return inputStr
	if(form == 'c'):
		return hexStrToCStyleLiteral( inputStr.encode("hex") )
	if(form == "hex"):
		return inputStr.encode("hex")
	return inputStr

def hexStrToCStyleLiteral(inputStr):
	print inputStr
	outputStr = ""
	count = 0
	for i in reversed(inputStr):
		outputStr = i + outputStr
		count = count + 1
		if (count % 2 == 0):
			outputStr = "\\x" + outputStr

	if(count % 2 != 0):
			outputStr = "\\x" + outputStr

	return outputStr

def hexStrToAscii(inputStr):
	return inputStr.decode("hex")

def xorChunk(inputStr, key):
	chunknum = int(inputStr.encode("hex"), 16) ^ key
	chunk = "%0.2x" % chunknum
	return chunk

def xorString(inputStr, key, keySize):
	outputStr = ""
	chunk = ""
	if(keySize == 0):
		return inputStr

	for i in inputStr:
		chunk += i
		if(len(chunk) == keySize):
			outputStr = outputStr + xorChunk(chunk, key)
			chunk = ""

	# Do last chunk!
	if(chunk != ""):
		outputStr = outputStr + xorChunk(chunk, key)

	return outputStr

def getKeyValue(inputStr):
	outputNum = 0
	tempStr = "" 
	if(len(inputStr) >= 3):
		if(inputStr[0:2] == "0x"):
			tempStr = inputStr.replace("0x", "")
			outputNum = int(tempStr, 16)
	else:
		outputNum = int(inputStr, 10)

	return outputNum

def getCharKeySize(inputNum):
	outputNum = 0
	while inputNum != 0:
		inputNum = inputNum >> 8
		outputNum = outputNum + 1
	return outputNum

def main():
	keyVal = ""
	keySize = ""
	keyStr = ""
	inputText = ""
	outputText = ""
	ofile = ""
	ifile =""
	form = ""
	try:
		opts, args = getopt.getopt(sys.argv[1:], "k:i:o:f:h", ["key=", "infile=", "outfile=", "format=", "help"])
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		print HELP
		sys.exit(2)
	for o, a in opts:
		if o in ("-i", "--infile"):
			ifile = a
		elif o in ("-o", "--outfile"):
			ofile = a
		elif o in ("-k", "--key"):
			keyStr = a
		elif o in ("-f", "--format"):
			form = a
		elif o in ("-h", "--help"):
			print HELP
			sys.exit(1)
		else:
			pass

	if(keyStr == ""):
		print "Error, no key specified.\n" + HELP
		sys.exit(3)

	if(ifile == ""):
		try:
			inputText = sys.stdin.read()
		except:
			print "Error reading from stdin"
			sys.exit(6)
	else:
		try:
			newFile = open(ifile, "r", -1);
			inputText = newFile.read()
		except:
			print "Error reading file " + ifile
			sys.exit(4)

	if(inputText == ""):
		print "Error, input string is blank"
		sys.exit(7)

	keyVal = getKeyValue(keyStr)
	keyNum = getCharKeySize(keyVal)
	#print "Key value is: " + str(keyVal)
	#print "Key num is: " + str(keyNum)
	#print "Input str is: " + inputText
	outputText = hexStrToAscii( xorString(inputText, keyVal, keyNum) )
	#print "hex output str is: " + TEXT2
	#print "And xored again is: " + hexStrToAscii( xorString(hexStrToAscii(TEXT2), keyVal, keyNum) )

	outputText = formatText( outputText, form)

	if(ofile == ""):
		print outputText
	else:
		try:
			newFile = open(ofile, "w", -1);
			newFile.write( outputText )
		except:
			print "Error writing to file " + ofile
			sys.exit(5)
				
main()
