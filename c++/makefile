CFLAGS := -m32

all: vtt_study

vtt_study.o: vtt_study.cpp
	g++ ${CFLAGS} -c vtt_study.cpp

vtt_study: vtt_study.o
	g++ vtt_study.o -o vtt_study

clean:
	rm -f *.o vtt_study
