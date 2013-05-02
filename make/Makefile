THINGS=printfunc.o library.a yourprogram

all: yourprogram

# NOTE: You can't print things anywhere!  Use echo keyword under a target to print things!

# You can do for loops like so, spacing
# and the use of the \ operator important! a for loop
# must be interpreted as one command with the \s.
# The $? operator will use ALL dependencies listed regardless
# of how new they are compared to the target (which isn't even
# a file)
printTargets: $(THINGS)
	echo "Here are some targets in the file:"
	for i in $^; \
	do echo " $$i "; done

# .o files are implicit rule, but here I state it as a target EXPLICITLY
# This is technically not needed, but I can control things like compiler to use and options
printfunc.o:
	gcc -c printfunc.c -o printfunc.o

# To create arithmetic.a, make needs to create int_arithmetic.o
# and does this through an IMPLICIT RULE.  Make sees the .o
# extension and knows the corresponding c file must be compiled.
# I didn't need to specify a target
library.a: int_arithmetic.o printfunc.o
	ar rc library.a int_arithmetic.o printfunc.o

# if -l shortcut is used, gcc wants library to be prepended
# with "lib", also wants L to provide library directories
# Make sure c files listed before libraries and output file
# An equivalent:
# gcc main.c ./library.a -o $@
# The $@ variable is the target name
yourprogram: library.a
	gcc main.c -L. -lrary -o $@

clean:
	rm -f *.o *.a yourprogram
