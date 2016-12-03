#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>

int main(){
  int c,l,m,ind, clientSocket,i,j,k;
  char  key[100]={'l','d','a','o','k','b','c','e','p','g','h','f','m','n','i','j','t','u','q','r','s','x','y','z','v','w'};
  char table[30][30];
 
 


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
  for ( i = 0; i < 26; ++i)
  {
    c=i;
    for (j = 0; j < 26; ++j)
    {
      table[i][j]=c+'a';
      c++;
      c=c%26;
    }
  }
  
  for ( i = 0; i < strlen(buffer); ++i)
  {

    if(buffer[i]==' ')
      continue;
    
    for ( k = 0; k < 26; ++k)
    {
     
      if(table[key[i%26]][k]==buffer[i]){
        buffer[i]=k+'a';
        printf("%d\n", k);
        break;
      
      }
    }

  }
  

  printf("\n\n  Data received: %s",buffer);   

  return 0;
}