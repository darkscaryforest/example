#include <stdio.h>
// Needed for int8_t
#include <stdint.h>

int main()
{
	int8_t w = 0x45;
	int8_t v = 0x98;
	int8_t z = 0x59;
	printf("1.To convert a portion to zero use AND, to convert a portion to F use OR, to preserve a portion use either:\n" \
		"   Anding a 4 bit number with 0xF preserves the number\n" \
		"   Anding a 4 bit number with 0x0 converts the to 0\n" \
		"   Oring a 4 bit number with 0xF converts the number to 0xF\n" \
		"   Oring a 4 bit number with 0x0 preserves the number.\n");
	printf("2: An 8bit integer w is 0x%x.\n   (w & 0x0F) = : 0x%x\n" \
		"   (w & 0xF0) = : 0x%x\n" \
		"   (w | 0x0F) = : 0x%x\n" \
		"   (w | 0xF0) = : 0x%x\n", w, (w & 0x0F), (w & 0xF0), (w | 0x0F), (w | 0xF0));
	printf("3: We have w = 0x%x and v = 0x%x. Want to have z = 0x%x\n" \
		"   (w << 4 & 0xF0) | (v >> 4 & 0x0F) = : 0x%x\n", w, v, z, (w << 4 & 0xF0) | (v >> 4 & 0x0F) );

	return 0;
}
