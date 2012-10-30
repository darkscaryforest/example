#!/bin/bash

# Make sure there's no space in between the equal and parathensis
VARARRAY=( 'one' 'two' 'three' 'four')

echo "1. Here is a printout of our array: ${VARARRAY[*]}."
echo "2. The second member is ${VARARRAY[1]}."
echo "3. In total, there are ${#VARARRAY[*]} members in the array."
echo "4. The length of the second member is ${#VARARRAY[1]}."
echo "5. Print the last 2 elements: ${VARARRAY[*]:2}"
