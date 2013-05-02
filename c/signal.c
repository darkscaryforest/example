#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void sighandler(int sig);

void main() {
	int i = 0;
	sigset_t newSet, oldSet;
	if(signal(SIGINT, sighandler) == SIG_ERR) {
		fprintf(stderr, "Failed to set signal handler");
		exit(1);
	}

	sigemptyset(&newSet);
	sigemptyset(&oldSet);
	sigaddset(&newSet, SIGINT);
	sigprocmask(SIG_BLOCK, &newSet, &oldSet);
	// REMEMBER: when a signal is blocking, received signals are NOT
	// dropped, they are just handled after we stop blocking!
	// However, sending multiple of the same signal during blocking seems
	// to cause only one to be handled after unblock...
	printf("signal now blocking! ctrl-c will be ignored until we unblock!\n");
	for(i = 0; i < 15; i++) {
		sleep(1);
	}
	sigprocmask(SIG_UNBLOCK, &newSet, &oldSet);
	printf("signal no longer blocking!\n");
	for(i = 0; i < 15; i++) {
		sleep(1);
	}
}

void sighandler(int sig) {
	printf("Caught signal\n");
}
