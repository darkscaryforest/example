all: parsefile bitwise pointers printf

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

printf: printf.o
	gcc printf.o -o printf

printf.o: printf.c
	gcc -c printf.c

clean:
	rm -f *.o parsefile bitwise pointers printf
