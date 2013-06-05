#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>

#define PORT			17009
#define TCP_SOCKET_ERROR	-1
#define PASSWORD		"SPICECONFETTI"
#define INCORRECT_MSG		"Incorrect password."
#define CORRECT_MSG		"You gave the correct password"
#define BUFFER_SIZE		256

int setup_server(int port); 

int main(int argc, char **argv) {
	int connfd = -1, listenfd = -1;
	unsigned int len = 0;
	char buff = malloc(sizeof(char) * BUFFER_SIZE + 1);
	memset(buff, 0x0, BUFFER_SIZE+1);
  	listenfd = setup_server(PORT); 
	while( 1 ) {
        	printf("socket in place awaiting connection...\n");
        	if( (connfd = accept(listenfd, (struct sockaddr *)NULL, NULL)) < 0) {
            		perror("Error accepting client connection.\n");   
            		return TCP_SOCKET_ERROR;            
        	}

		len = read(connfd, buff, BUFFER_SIZE);
		if(len < strlen(PASSWORD) || (strncmp(buff, PASSWORD, strlen(PASSWORD)) == 0)) {
			write(listenfd, INCORRECT_MSG, strlen(INCORRECT_MSG));
		} else {
			write(listenfd, CORRECT_MSG, strlen(CORRECT_MSG));
		}

		close(connfd);
	}

	return 0;
}

int setup_server(int port) {  
        int listenfd;
        struct sockaddr_in servaddr;
            
        printf("Setting up tcp socket on port %u\n", port);
                                                
        bzero(&servaddr, sizeof(servaddr));
        servaddr.sin_family = AF_INET;                                      
        servaddr.sin_addr.s_addr = htons(INADDR_ANY);//htonl(INADDR_ANY);
        servaddr.sin_port = htons(port);

        if( (listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
            perror("Error setting up socket\n");
            return TCP_SOCKET_ERROR;
        }
        
        if(bind(listenfd, (struct sockaddr *) &servaddr, sizeof(servaddr)) < 0) {
            perror("Error binding\n");
            return TCP_SOCKET_ERROR;
        }   
            
        if(listen(listenfd, 1024) < 0) {
            perror("Error listening on port\n");
            return TCP_SOCKET_ERROR;
        }
            
        return listenfd;
}

