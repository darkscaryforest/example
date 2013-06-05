CC=gcc
BINARIES=parsefile bitwise pointers strings printf hex_tofrom_str random signal server
CLEANEES=$(BINARIES)

all: $(BINARIES)

# Remember that $@ refers to the target (parsefile)
# and $? is dependencies newer than the target just the (parsefile.o listed)
parsefile: parsefile.o
	$(CC) $? -o $@

parsefile.o: parsefile.c
	$(CC) -c parsefile.c

bitwise: bitwise.o
	$(CC) $? -o $@

bitwise.o: bitwise.c
	$(CC) -c bitwise.c

pointers: pointers.o
	$(CC) $? -o $@

pointers.o: pointers.c
	$(CC) -c pointers.c

strings: strings.o
	$(CC) $? -o $@

strings.o: strings.c
	$(CC) -c strings.c

printf: printf.o
	$(CC) $? -o $@

printf.o: printf.c
	$(CC) -c printf.c

random: random.o
	$(CC) $? -o $@

random.o: random.c
	$(CC) -c random.c

server: server.o
	$(CC) $? -o $@

server.o: server.c
	$(CC) -c server.c

# For the sake of example, the target for signal.c actually isn't needed 
# since .o files are an extension that applies for implicit rules!
# see make examples for more info
signal: signal.o
	$(CC) $? -o $@

# Needs the math library (m), specified by -lm
hex_tofrom_str: hex_tofrom_str.o
	$(CC) $? -o $@ -lm

hex_tofrom_str.o: hex_tofrom_str.c
	$(CC) -c hex_tofrom_str.c

clean:
	rm -f *.o $(CLEANEES)
