#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
// This header file is from the math library, so we have to include it while linking!!!
#include <math.h>

void hexstr_to_intarray(char *idstr, uint8_t *id, uint32_t arraysize);
void intarray_to_hexstr(uint8_t *id, char *idstr, uint32_t arraysize);

int main() {
	int i;
	char *hexstr = "3e55abcd";
	char *hexstr2; 
	uint32_t ksize = ceil((double)strlen(hexstr)/2);
	uint8_t k[ ksize ];
	hexstr2 = malloc(sizeof(char) * ksize * 2 + 1);
	hexstr_to_intarray(hexstr, k, ksize);
	printf("1. This is a hexstr: %s, after we convert this to an array of unsigned integers we can print like so:\n", hexstr);
	for(i = ksize - 1; i >= 0; i--) {
		printf("%u ", k[i]);
	}
 	intarray_to_hexstr(k, hexstr2, ksize);
	printf("\n2. Converting this back to a string: %s\n", hexstr);
	free( hexstr2 );
	return 0;
}

void hexstr_to_intarray(char *idstr, uint8_t *id, uint32_t arraysize)
{
	uint32_t i, len = strnlen(idstr, arraysize*2);
	int offset = arraysize*2 - len;
	char idstr_cpy[arraysize * 2 + 1];
	char temp[3];

	memset(id, 0, arraysize);
	memset(idstr_cpy, 0x30, len);
	memcpy(idstr_cpy + offset, idstr, len);
	idstr_cpy[len] = '\0';
	temp[2] = '\0';

	for(i = 0; i < arraysize; i++)
	{
		memcpy(temp, idstr_cpy + (i*2), 2);
		id[arraysize - 1 - i] = strtoul(temp, NULL, 16);
	}
}

void intarray_to_hexstr(uint8_t *id, char *idstr, uint32_t arraysize)
{
	uint32_t i, num;
	char temp[3];
	temp[2] = '\0';
	memset(idstr, 0x30, arraysize*2);
	for(i = 0; i < arraysize; i++)
	{
		num = id[arraysize - 1 - i];
		snprintf(temp, 3, "%x", num);
		if(num < 16)
		{
			temp[1] = temp[0];
			temp[0] = 0x30;
		}
		memcpy(idstr + (i*2), temp, 2);
	}
}
