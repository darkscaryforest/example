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
# one, two, and three.  NOTE: to define new make syntax like these targets,
# we NEED to wrap it with the eval function
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

# illustrates the fact that functions without eval really just return a string
# made up of the function body
.PHONY: funcprint
FUNCPRINT := $(call bluntprint,test)
# functions without eval can help with shorting string parsing though
FUNCPRINT2 := $(call parseprint,test)
funcprint:
	@echo $(FUNCPRINT)
	@echo "Misleading is $(MISLEADING)"
	@echo $(FUNCPRINT2)

CHANGE := one
# Make will think PLUS is a recursive variable and hold off on
# evaluating CHANGE until it's used in a target
PLUS += $(CHANGE)
CHANGE := two
# Tells make that PLUS2 is a non-recursive variable,
# so evaluate CHANGE immediately on the plus equal assignment
PLUS2 :=
PLUS2 += $(CHANGE)
CHANGE := three

.PHONY: plusequal
plusequal:
	@echo "$(PLUS) and $(PLUS2)"

# Code to create a recursive list of directories, and mkdir them
# (implementing a mkdir -p essentially)
DIRECTORY := one/two/three/four
PATHWAYS :=
$(foreach i,$(subst /, ,$(DIRECTORY)), \
	$(eval $(call buildpath,$(i))))

.PHONY: directory
directory:
	@echo $(PATHWAYS)
	mkdir $(PATHWAYS)

clean:
	rm -f *.o *.a yourprogram

.PHONY: addontarget addontargetagain moreaction
# Specifying double colons lets you declare the same target
# multiple time to add on actions
addontarget::
	@echo "Print this"

addontarget::
	@echo "Print that"

# in case you need to add onto a target that can't have double colons
# you can always tack on more dependencies like this
# (which we've been doing to special target .PHONY all along)
addontargetagain:
	@echo "This target might be defined in a file you can't change"

addontargetagain: moreaction

moreaction:
	@echo "Print this too, but will print first"
