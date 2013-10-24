# This makefile will essentially be pasted into the makefile
# that includes it

define myfunc

# This let's make know that whatever $(1) is
# won't be a target representing a real file
.PHONY: $(1)

# In a user defined function, you have to double dollar
# sign user variables to get them to function correctly
$(1): $(2)
	@echo "$$@ and $$^"

endef
