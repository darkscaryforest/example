#!/bin/bash

VAR1="teststring"
VARARRAY=( 'one' 'two' 'three' 'four')

i=0
echo "1. A while loop prints something 5 times:"
while [ ${i} -lt 5 ]
do
	echo "${VAR1} print ${i}"
	# Does NOT work, treats i as string
	# i=${i}+1
	# way to increment i
	let i=i+1
done

echo "2. The following is a for loop printing each element in an array:"
for i in ${VARARRAY[*]}
do
	echo "Array element ${i}" #${VARARRAY[i]}
done
