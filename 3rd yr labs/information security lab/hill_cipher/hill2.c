#include<stdio.h>
#include<conio.h>
int n,i,len,j,m,l,ptxt[3][3],k[3][3],aa[3];
char pt[20],ct[20],rf[20];
void getd();
void display1();
void encrypt();
void decrypt();
int select(int);
int euclid(int,int);
int display();
void main(){
	int c;
	do{
		clrscr();
		f1:
		display();
		printf(“Enter Your Choice:”);
		scanf(“%d”,&c);
		
		if(c>4 || c<1){
			clrscr();
			printf(“\nEnter proper value\n”);
			goto f1;
		}
		select(c);
	}while(c!=4);
	getch();
}
int display(){
	printf(“Hill Cipher program\n”);
	printf(“———————–\n”);
	printf(” option Functions\n”);
	printf(“———————–\n”);
	printf(” [1] Enter The Text\n”);
	printf(” [2] Encrypted Text\n”);
	printf(” [3] Decrypted Text\n”);
	printf(” [4] Exit\n”);
	printf(“———————–\n”);
	return 0;
}
int select(int c){
	int i;
	switch(c){
		case 1:{clrscr();
			display();
			fflush(stdin);
			getd();
			display1();
			for(i=0;ct[i]!=”;i++)
				ct[i]=”;
			break;
		}
		case 2:{clrscr();
			display();
			encrypt();
			break;
		}
		case 3:{clrscr();
			display();
			decrypt();
			break;
		}
		case 4: break;
	}
	return c;
}
void getd(){
	printf(“Enter the plain text:”);
	gets(pt);
	printf(“Ente the key in number associate alphabet:\n”);
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			f: printf(“k[%d][%d]= “,i,j);
			scanf(“%d”,&k[i][j]);
			if(k[i][j]>25 || k[i][j]<0){
				printf(“Enter Wrong Value reenter”);
				goto f; } }  }  }
				void display1(){
					printf(“plain text:%s\n”,pt);
					printf(“key:\n”);
					for(i=0;i<3;i++){
						for(j=0;j<3;j++){
							printf(“%3d”,k[i][j]);}
							printf(“\n”);
						}
					}
					void encrypt(){
						
						j=0;
						l=n=0;
						len=strlen(pt);
						for(i=0;i<len;){
							for(m=0;m<3;m++,i++){
								if(i>len) ptxt[m][0]=0;
								else ptxt[m][0]=abs((65-pt[i]));
							}
							for(j=0;j<3;j++,n++){
								aa[j]=0;
								for(l=0;l<3;l++)
									aa[j]=aa[j]+(k[j][l]*ptxt[l][0]);
								ct[n]=(65+(aa[j]%26));
							}
						} ct[n]=”;
						printf(“\n%s”,ct);
						getch();
					}
					int euclid(int a,int b)
					{
						int r1,r2,t1,t2,q,r,t,inverse,temp;
						if(a<b){
							temp=b;
							b=a;
							a=temp;
						}
						r1=a;
						r2=b;
						t1=0;
						t2=1;
						while(r2!=0)
						{
							q=r1/r2;
							r=r1%r2;
							t=t1-(q*t2);
							t1=t2;
							t2=t;
							r1=r2;
							r2=r;
						}
						inverse=t1%t2;
						if(inverse<0)
						{
							inverse=inverse+t2;
						}
						return inverse;
					}
					void decrypt()
					{ int b[3],in[3][3],det,abc,d1;
						det=k[0][0]*(k[1][1]*k[2][2]-k[2][1]*k[1][2])-k[0][1]*(k[1][0]*k[2][2]-k[1][2]*k[2][0])+k[0][2]*(k[1][0]*k[2][1]-k[1][1]*k[2][0]);
						abc=det;
						if(abc<0) det=26-((abs(abc))%26);
						else det=(abc%26);
						det=euclid(det,26);
						printf(“\n Determinant :%d \n”,det);
						in[0][0]=((k[1][1]*k[2][2])-(k[2][1]*k[1][2]));
						in[1][0]=-((k[1][0]*k[2][2])-(k[1][2]*k[2][0]));
						in[2][0]=((k[1][0]*k[2][1])-(k[2][0]*k[1][1]));
						in[0][1]=-((k[0][1]*k[2][2])-(k[0][2]*k[2][1]));
						in[1][1]=((k[0][0]*k[2][2])-(k[0][2]*k[2][0]));
						in[2][1]=-((k[0][0]*k[2][1])-(k[2][0]*k[0][1]));
						in[0][2]=((k[0][1]*k[1][2])-(k[0][2]*k[1][1]));
						in[1][2]=-((k[0][0]*k[1][2])-(k[1][0]*k[0][2]));
						in[2][2]=((k[0][0]*k[1][1])-(k[1][0]*k[0][1]));
						printf(“\n Inverse is : \n”);
						for(i=0;i<3;i++){
							for(j=0;j<3;j++) {
								if(in[i][j]<0) in[i][j]=26-((abs(in[i][j]))%26);
								else in[i][j]=(in[i][j]%26);
								in[i][j]=((in[i][j]*det)%26);
								printf(“%4.2d “,in[i][j]);}
								printf(“\n”);  }
								len=strlen(ct);
								j=0;
								l=n=0;
								for(i=0;i<len;){
									for(m=0;m<3;m++,i++){
										if(i>len) ptxt[m][0]=0;
										else
											ptxt[m][0]=abs((65-ct[i]));
										printf(“%2d “,ptxt[m][0]); }
										printf(“\n”);
										for(j=0;j<3;j++,n++){
											b[j]=0;
											for(l=0;l<3;l++)
												b[j]=b[j]+((in[j][l]*ptxt[l][0]));
											aa[j]=b[j];
											rf[n]=(65+((26+aa[j])%26));  }  }
											rf[n]=”;
											for(i=0;i<strlen(ct);i++)
												printf(“%c”,rf[i]);
											getch();
										}