#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	// Memory was automatically allocated and a null terminator was put at the end of this string literal.
	char *s = "this is a string";
	// Counts characters until encountering the null terminator, the length doesn't include the null terminator
	int s_count = strlen(s);
	// When we allocate, we *must* account for the null terminator!!!
	char *t = malloc( s_count + sizeof(char) );
	strcpy(t, s);
	// strncpy lets you specify the amt to cpy, and pads any remaining space with null terminators
	printf("1. This is a string literal: %s, which was copied into this dynamically allocated string: %s\n", s, t);
}
