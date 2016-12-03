int array[100] ;
sendto(sockfd, array, sizeof(array), 0, &addr, addrlen);



int array[100] ;
recvfrom(sockfd, array, sizeof(array), 0, &addr, &addrlen);