THINGS=printfunc.o library.a yourprogram

all: yourprogram one two three

include ./extend.mk

# NOTE: You can't print things anywhere!  Use echo keyword under a target to print things!

DEMO := down
# This is a recursive assignment, meaning that any other variables in the
# assignment aren't resolved until it is actually used. Thus, if $(TEST)
# is used as an action for a target, it will be used after the rest of the entire
# makefile(s) is/are processed
TEST = $(DEMO)
# This assignment is non-recursive, any other variables in it are resolved 
# immediately
TEST2 := $(DEMO)
VARS := one two three
# This calls our user defined function and defines a brand new targets
# one, two, and three
$(foreach i, $(VARS), \
	$(eval $(call myfunc,$(i),test)))

# This will be called by one, two, and three
# Putting the @ sign before a command prevents make from printing the
# command itself. This makes sense for echo, since it is going to print
# the following string anyways. (so @echo prints only once)
.PHONY: test
test:
	@echo "The recursive var: $(TEST) and non-recursive var: $(TEST2)"

DEMO := up

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
