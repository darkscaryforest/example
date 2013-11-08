# This makefile will essentially be pasted into the makefile
# that includes it

define myfunc

# This let's make know that whatever $(1) is
# won't be a target representing a real file
.PHONY: $(1)

# When using eval function, you may have to use double dollar
# sign on user variables to get them to function correctly
# eval wants to immediately resolve all variables when forming
# the new syntax. variables $(1) and $(2) should work fine
# since those arguments have already been passed.. but $@ and $^
# are special variables dependent on the target..which won't be
# resolved til the target is hit at the end
#
# So we escape them with an extra dollar sign, so that eval
# maintains them as $@ and $^
# ANOTHER_VAR needs the escape too, because it hasn't actually been
# defined yet as eval is going through to resolve all variables.
# ANOTHER_VAR's assignment is in the very body that eval must resolve first
ANOTHER_VAR := "more text"
$(1): $(2)
	@echo "$$@ and $$^ and $$(ANOTHER_VAR)"

endef

# function to assist with directory target implementing mkdir -p
define buildpath
TEMP_DIR+=$(1)/
space :=
space +=
TEMP_DIR := $$(subst $$(space),,$$(TEMP_DIR))
PATHWAYS += $$(TEMP_DIR)
endef

# Without eval, this is actually going to return the string "MISLEADING += test"
# instead of setting MISLEADING
define bluntprint
MISLEADING += $(1)
# If there was another command here there would be a syntax error
endef

define parseprint
$(subst e,E,$(1))
endef
