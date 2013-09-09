#!/bin/python
import sys, encodings, math, binascii

def main():
	num = 703437
	asciiNum = intToAscii(num)
	hexStrAsciiNum = asciiToHexStr(asciiNum)
	hexStrNum = intToHexStr(num)
	binStrNum = intToBinStr(num)
	asciiBinStr = asciiToBinStr("0a0a")
	print "NOTE: BINARY STR, HEX STR, and ASCII are essentially the same thing."
	print "1. We have the DECIMAL INT number " + asciiNum \
		+ "\nwhich was converted to ASCII to display it."
	print "2. Converting the ASCII form to HEX STR displays " + hexStrAsciiNum + "\n" \
		+ "but thats actually the HEX STR representation of the ASCII values\n" \
		+ "of DECIMAL INT " + asciiNum + "."
	print "3. We can go directly from DECIMAL to HEX STR: " + hexStrNum
	print "4. Likewise, we can go quickly from HEX STR to DECIMAL INT:"
	print hexStrToInt(hexStrNum)
	print "5. From DECIMAL INT to BINARY STR (padded leftmost with enough zeros\n" \
		+ "for a byte) we have " + binStrNum
	print "6. BINARY STR to DECIMAL INT:"
	print binStrToInt(binStrNum)
	print "7. Of course, using the above functions we can go from HEX STR to\n" \
		+ "BINARY STR and vice versa giving "+ intInHexStrToIntInBinStr(hexStrNum) \
		+ "\nand " + intInBinStrToIntInHexStr(binStrNum) + " respectively.\n" \
		+ "Note that this is technically these representations are of the\n" \
		+ "original DECIMAL INT and not the ASCII strings themselves."
	print "8. To get the actual BINARY STR represention of an ASCII STR...\n" \
		+ "take the string 0a0a for example, it becomes " + asciiBinStr + "\n" \
		+ "and the reverse is " + binStrToAscii(asciiBinStr)
	print "9. Having a DECIMAL INT in ASCII like " + asciiNum + " can be quickly\n" \
		+ "converted to the same int as a BINARY STR: \n" \
		+ intInAsciiToIntInBinStr(asciiNum) + " and the reverse:\n" \
		+ intInBinStrToIntInAscii( intInAsciiToIntInBinStr(asciiNum) )

	return 0

def intToAscii(input):
	return str(input)

def intInAsciiToInt(input):
	# NOTE: Name has "intIn", to reduce ambiguity. We need to take in an ascii string
	# actually representing an integer
	return int(input)

def hexStrToAscii(input):
	# alternative: binascii.unhexlify(input)
	return input.decode("hex")

def asciiToHexStr(input):
	# alternative: binascii.hexlify(input)
	return input.encode("hex")

def intToHexStr(input):
	hexStr = "%x" % input
	if( len(hexStr) % 2 != 0 ):
		hexStr = "0" + hexStr
	return hexStr

def hexStrToInt(input):
	return int(input, 16)

def intToBinStr(input):
	# We get rid of the 0b prefix with brackets and zfill
	# will pad to the left with enough zeros to complete the leftmost byte
	return bin(input)[2:].zfill(8 * bytesToHoldInt(input))

def binStrToInt(input):
	return int(input, 2)

def intInBinStrToIntInHexStr(input):
	# NOTE: Actually converts to hex string of the int represented by binary str
	return intToHexStr( binStrToInt(input) )

def intInHexStrToIntInBinStr(input):
	# NOTE: Actually converts to binary string of the int represented by hex str
	return intToBinStr( hexStrToInt(input) )

def intInAsciiToIntInBinStr(input):
	return intToBinStr( intInAsciiToInt(input) )

def intInBinStrToIntInAscii(input):
	return intToAscii( binStrToInt(input) )

def asciiToBinStr(input):
	# NOTE: We are getting the hex values of each ascii character and converting that
	# to binary...as it would look in memory
	# alternative: bin(int(binascii.hexlify(input), 16))
	return intToBinStr( hexStrToInt( asciiToHexStr(input) ) )

def binStrToAscii(input):
	# alternative: binascii.unhexlify('%x' % int(input, 2))
	return hexStrToAscii( intToHexStr( binStrToInt(input) ) )

def bytesToHoldInt(input):
	# NOTE: does not actually return size of variable in memory
	return int((highestPowOfTwo(input) / 8) + 1)

def highestPowOfTwo(input):
	return int(math.log(input) / math.log(2))

main()
