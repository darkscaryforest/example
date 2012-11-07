#include <stdio.h>

int main() 
{
	int k = 1;
	unsigned int l = 254;
	double m = 3.3333333;
	char *n = "this is str";
	char o[10] = "second str";
	long int p = 2000000;
	long unsigned int q = 4000000;
	printf("1. Here are the ways to print an int: %d, an unsigned int: %u\n" \
		"   a double: %f, a hex value (unsigned int): %x\n" \
		"   a char *: %s, a char[]: %s, a single char: %c\n" \
		"   a long int: %ld, a long unsigned int: %lu\n", k, l, m, l, n, o, o[1], p, q);

	printf("2. Here are ways to escape characters: %%\n");

	printf("3. The syntax for a format placeholder is %%[parameter][flags][width][.precision][length]type\n" \
		"   Print m, width is 10 and precision is 2: %10.2f\n", m);

	printf("4. Here we pass the width = 3 and precision = 0 of m as args to printf using asterick: %*.*f\n", 3, 0, m);
}
