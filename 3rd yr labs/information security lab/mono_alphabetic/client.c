#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>

int main(){
  int ind, clientSocket,i,j,k;
  char  key[100]={'l','d','a','o','k','b','c','e','p','g','h','f','m','n','i','j','t','u','q','r','s','x','y','z','v','w'};

  char buffer[1024];
  struct sockaddr_in serverAddr;
  socklen_t addr_size;

  /*---- Create the socket. The three arguments are: ----*/
  /* 1) Internet domain 2) Stream socket 3) Default protocol (TCP in this case) */
  clientSocket = socket(PF_INET, SOCK_STREAM, 0);
  
  /*---- Configure settings of the server address struct ----*/
  /* Address family = Internet */
  serverAddr.sin_family = AF_INET;
  /* Set port number, using htons function to use proper byte order */
  serverAddr.sin_port = htons(7891);
  /* Set IP address to localhost */
  
  serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
  /* Set all bits of the padding field to 0 */
  memset(serverAddr.sin_zero, '\0', sizeof serverAddr.sin_zero);  

  /*---- Connect the socket to the server using the address struct ----*/
  addr_size = sizeof serverAddr;
  connect(clientSocket, (struct sockaddr *) &serverAddr, addr_size);

  /*---- Read the message from the server into the buffer ----*/
  recv(clientSocket, buffer, 1024, 0);

  /*---- Print the received message ----*/

  for ( i = 0; i < strlen(buffer); ++i)
  {
    if(buffer[i]==' ')
      continue;
    for ( j = 0; j < 26; ++j)
    {
      if(key[j]==buffer[i])
        ind=j;

    }
    
    buffer[i]='a'+ind;
  }

  printf("Data received: %s",buffer);   

  return 0;
}