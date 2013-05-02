#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define LOWER	5
#define UPPER	10

int main() 
{
	unsigned int q = 0;
	srand(time(NULL));
	q = LOWER + (rand() % (UPPER - LOWER));
	printf("1. A random number between 5 and 10: %u\n", q);
}
