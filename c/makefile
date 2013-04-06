all: parsefile bitwise pointers strings printf hex_tofrom_str

parsefile: parsefile.o
	gcc parsefile.o -o parsefile

parsefile.o: parsefile.c
	gcc -c parsefile.c

bitwise: bitwise.o
	gcc bitwise.o -o bitwise

bitwise.o: bitwise.c
	gcc -c bitwise.c

pointers: pointers.o
	gcc pointers.o -o pointers

pointers.o: pointers.c
	gcc -c pointers.c

strings: strings.o
	gcc strings.o -o strings

strings.o: strings.c
	gcc -c strings.c

printf: printf.o
	gcc printf.o -o printf

printf.o: printf.c
	gcc -c printf.c

# Needs the math library (m), specified by -lm
hex_tofrom_str: hex_tofrom_str.o
	gcc hex_tofrom_str.o -o hex_tofrom_str -lm

hex_tofrom_str.o: hex_tofrom_str.c
	gcc -c hex_tofrom_str.c

clean:
	rm -f *.o parsefile bitwise pointers strings printf hex_tofrom_str
