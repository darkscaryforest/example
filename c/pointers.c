#include <stdio.h>
// Needed for malloc:
#include <stdlib.h>

#define BUF_SIZE 500

void swapfunc(int *a, int *b);
void pointerToPointer(char **k);

typedef struct {
	int elem1;
	char *elem2;
} tstruct;

int main() {
	printf("This program is all about pointers.\n");

	// Memory is allocated on the stack here for stro
	char stro[BUF_SIZE] = "This character array needs to have a size defined.";
	printf("1. stro is: %s\n", stro);

	// This character pointer is assigned the address of stro.
	// The star is used to indicate a pointer on declaration..but elsewhere used to dereference the pointer
	char *j = stro;
	printf("2. j points to stro: %s\n", j);

	// NOTE THAT %S WAS USED FOR BOTH THE CHAR[] AND CHAR *
	// PSA: An array degrades into a pointer.  char[] = char *
	// This does NOT work for multidimensional arrays char[][] != char **

	// This declares and initializes a pointer to a string literal. No manual memory allocation was needed.
	// However, the memory located at strp is not modifiable since it is a string literal
	char *strp = "This is unmodifiable string";
	printf("3. strp: %s\n", strp);

	// THIS IS BAD: (no memory is assigned to pointer!!)
	// int *k = 9; ...doesn't work like assigning string literal
	int k = 9;
	// Declare and initialize l to point to the address of k
	int *l = &k;
	// initializing separate from declaration SAME THING AS LINE ABOVE
	l = &k;
	printf("4. k is %d and l that points to is %d\n", k, *l);

	// Observed programming practice: ONLY USE MALLOC WHEN YOU HAVE TO
	int *m = malloc(sizeof(int));
	*m = 10;
	printf("5. m is integer pointer assigned memory with malloc: %d\n", *m);

	int a = 3;
	printf("6. Passing a = %d and m = %d into swap function. ", a, *m);
	// Pass in our params: a's address and the pointer m
	swapfunc(&a, m);
	printf("After swap a = %d and m = %d\n", a, *m);
	// Free memory!!
	free(m);

	tstruct tests = { 4, "testy"};
	tstruct *t = &tests;
	printf("7. A pointer to a struct uses arrows to access members: %d and %s\n", t->elem1, t->elem2);	

	j = "STRINGLITERAL";
	char *y = j+2;
	printf("8. If you want to change what a pointer points to in a function,\n"
		"   you have to pass a pointer to the pointer. j is %s\n" \
		"   y points to the 3rd letter %c\n", j, *y);
	// Pass address of the pointer
	pointerToPointer(&y);
	printf("   The function changed this to the 4th letter %c since we passed the pointer's address.\n", *y);
	
}

// Classic swap function
void swapfunc(int *a, int *b)
{
	// Save the value that a is pointing to in temp var
	int temp = *a;
	// Put the value that b points to as the value that a points to
	*a = *b;
	// Set the value that b points to as temp
	*b = temp;
}

void pointerToPointer(char **k)
{
	// Dereference to get the address of the pointer, then increment
	(*k)++;
}
