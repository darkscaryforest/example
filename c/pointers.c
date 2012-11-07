#include <stdio.h>
// Needed for malloc:
#include <stdlib.h>

#define BUF_SIZE 500

int main() {
	printf("This program is all about pointers.\n");
	// Memory is allocated on the stack here for stro

	char stro[BUF_SIZE] = "This character array needs to have a size defined.";
	printf("1. stro is: %s\n", stro);

	// This character pointer is assigned the address of stro.
	char *j = stro;
	printf("2. j points to stro: %s\n", j);

	// This declares and initializes a pointer to a string literal. No manual memory allocation was needed.
	// However, the memory located at strp is not modifiable since it is a string literal
	char *strp = "This is unmodifiable string";
	printf("3. strp: %s\n", strp);

	// THIS IS BAD: (no memory is assigned to pointer!!)
	// int *k = 9;
	int k = 9;
	// Declare and initialize l to point to the address of k
	int *l = &k;
	printf("4. k is %d and l that points to is %d\n", k, *l);

	// Observed programming practice: ONLY USE MALLOC WHEN YOU HAVE TO
	int *m = malloc(sizeof(int));
	*m = 10;
	printf("5. m is integer pointer assigned memory with malloc: %d\n", *m);
	// Free memory!!
	free(m);
	
}
