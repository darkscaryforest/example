#!/bin/bash

VAR1="teststring"
VAR2="anotherstring"

# The spaces are important in the next line!
if [ "${VAR1}" == "teststring" ]; then
	echo "1. Compared strings in if. VAR1 is equal to teststring"
# If you're using vim colors, VAR2 might show up as a literal string below...it isn't.  
# It is processed as a variable
elif [ "${VAR1}" == "${VAR2}" ]; then
	echo "equals anotherstring instead"
else
	echo "Not equal"
fi

VAR3=10
VAR4=
if [ ${VAR3} -eq 10 ]; then
	echo "2. VAR3 is equal to 10"
fi

if [ ${VAR3} -ne 100 ]; then
	echo "3. VAR3 is not equal to 100"
fi

if [ ${VAR3} -lt 100 ]; then
	echo "4. VAR3 is less than 100"
fi

if [ ${VAR3} -gt 5 ]; then
	echo "5. VAR3 is greater than 5"
fi

if [ ${VAR3} -ge 10 ]; then
	echo "6. VAR3 is greater than OR equal to 10"
fi

if [ ${VAR3} -le 10 ]; then
	echo "7. VAR3 is less than OR equal to 10"
fi

if [ -z "${VAR4}" ]; then
	echo "8. VAR4 has a string length of zero"
fi

VAR4=1
if [ -n "${VAR4}" ]; then
	echo "9. VAR4 now has a string length greater than zero"
fi

if [ -e "example.txt" ]; then
	echo "10. The file \"example.txt\" exists in this directory."
fi
