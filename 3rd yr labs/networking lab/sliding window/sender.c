#include<stdio.h>
#include<sys/socket.h>
#include<sys/types.h> 
#include<netinet/in.h> 
#include<string.h> 
#include<stdlib.h> 
#include<arpa/inet.h> 
#include<unistd.h>
#define SIZE 4

int main() {

	unsigned int sfd,lfd,len,i,j,status;
	char str[20],frame[20],temp[20],ack[20]; 
	struct sockaddr_in saddr,caddr; 
	sfd=socket(AF_INET,SOCK_STREAM,0);
	
	//The socket() function tells our OS that we want
	//a file descriptor for a socket 
	//which we can use for a network stream connection; 

	if(sfd<0)
	perror("Error"); 
	
	bzero(&saddr,sizeof(saddr)); 
	
	saddr.sin_family=AF_INET; 
	saddr.sin_addr.s_addr=htonl(INADDR_ANY); 
	saddr.sin_port=htons(9001);
	
	// we create it with information
	// about the server, and then we bind()
	// it to the socket.
	
	if( bind(sfd,(struct sockaddr*)&saddr,sizeof(saddr)) < 0 ) 
	perror("Bind Error");
	
	// The listen() function then tells our program to 
	// start listening using the given socket. The second
	// parameter of listen() allows us to specify the maximum
	// number of connections that can be queued. 
	listen(sfd,5); 
	len = sizeof(&caddr);
	
	lfd=accept( sfd, (struct sockaddr*)&caddr, &len); 
	printf(" Enter the text : \n"); 
	scanf("%s",str);
	i=0; 

	while(i<strlen(str)) {
		memset(frame,0,20); 
		strncpy(frame,str+i,SIZE); 
		printf(" Transmitting Frames. "); 
		len=strlen(frame); 
		for(j=0;j<len;j++)
		{
			printf("%d",i+j); 
			sprintf(temp,"%d",i+j); 
			strcat(frame,temp);
		} 

		printf("\n");
		//write(lfd,frame,sizeof(frame));
		frame[strlen(frame)]='\0';
		printf("\n frame= %s\n", frame); 
		send(lfd,frame,strlen(frame),0);
		recv(lfd,ack,1024,0);	 
		
		//send(connected,fr,strlen(fr),0);
		//recv(sock,data,1024,0);	 
		
		//read(lfd,ack,20); 
		sscanf(ack,"%d",&status);
		
		if(status==-1)
		printf(" Transmission is successful. \n"); 
		
		else
		{
			printf(" Received error in %d \n\n",status); 
			printf("\n\n Retransmitting Frame. ");
			memset(frame,0,20);
			for(j=0;;)
			{
				frame[j]=str[j+status]; 
				printf("%d",j+status); 
				j++;
				
				if((j+status)%4==0) 
				break;
			} 
			printf("\n"); 
			frame[j]='\0';
			len=strlen(frame); 
			
			for(j=0;j<len;j++) {
				sprintf(temp,"%d",j+status); 
				strcat(frame,temp);
			} 
			//write(lfd,frame,sizeof(frame));
			frame[strlen(frame)]='\0';
			printf("\n frame= %s\n", frame); 
		
			send(lfd,frame,strlen(frame),0);
			sleep(2); 
	
		}

		i+=SIZE;
	} 

//	write(lfd,"exit",sizeof("exit")); 
	send(lfd,"exit",sizeof("exit"),0);
	printf("Exiting\n");
	sleep(2); 
	close(lfd); 
	close(sfd);

}