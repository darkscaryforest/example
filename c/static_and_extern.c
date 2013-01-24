#include <stdio.h>

// This is a global variable.
// The extern keyword can be used elsewhere to reference this guy
int globalvar1;

int main()
{
	static int staticvar = 0;
	
	return 0;
}

// Using static on a function makes it private to this compilation unit.
// No other unit can use this, even if we put it in a header for them.
static void staticfunc
{
}
