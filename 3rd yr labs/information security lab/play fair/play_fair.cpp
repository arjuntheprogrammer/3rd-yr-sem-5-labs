
#include<bits/stdc++.h>
#include <time.h>

using namespace std;
 main() {
	char v,w,ch,string[100],arr[5][5],key[10]="monarchy",a,b,enc[100];
	int temp,i,j,k,l,r1,r2,c1,c2,t,var;
	t = clock();
	FILE * fp;
	fp=fopen("text.txt","r");
	//printf("Enter the key\n");
	//scanf("%s",&key);

	l=0;
	while(1) {
		ch=fgetc(fp);
		if(ch!=EOF) {
			string[l++]=ch;
		}
		if(ch==EOF) 
		    break;
	}
	string[l]='\0';
	puts(string);

	for (i=0;key[i]!='\0';i++) {
		for (j=i+1;key[j]!='\0';j++) {
			if(key[i]==key[j]) {
				temp=1;
				break;
			}
		}
	}
	if(temp==1) 
	printf("invalid key"); else {
		k=0;
		a='a';
		//printf("%c",b); 
		for (i=0;i<5;i++) {
			for (j=0;j<5;j++) {
				if(k<strlen(key)) 
				    arr[i][j]=key[k]; 
				else if(k==strlen(key)) {
					b: 
					for (l=0;l<strlen(key);l++) {
						if(key[l]==a) {
							a++;
							goto b;
						}
					}
					arr[i][j]=a;
					if(a=='i') 
					    a=a+2; else 
					    a++;
				}
				if(k<strlen(key)) 
				    k++;
			}
		}
		printf("\n");
		printf("The matrix is\n");
		for (i=0;i<5;i++) {
			for (j=0;j<5;j++) {
				printf("%c",arr[i][j]);
			}
			printf("\n");
		}
		t=0;
		if(strlen(string)%2!=0) 
		var=strlen(string)-1;
		for (i=0;i<var;) {
			v=string[i++];
			w=string[i++];
			if(v==w) {
				enc[t++]=v;
				enc[t++]='$';
			} else {
				for (l=0;l<5;l++) {
					for (k=0;k<5;k++) {
						if(arr[l][k]==v||v=='j'&&arr[l][k]=='i') {
							r1=l;
							c1=k;
						}
						if(arr[l][k]==w||w=='j'&&arr[l][k]=='i') {
							r2=l;
							c2=k;
						}
					}
				}
				if(c1==c2) {
					r1=(r1+1)%5;
					r2=(r2+1)%5;
					
				} else if(r1==r2) {
					c1=(c1+1)%5;
					c2=(c2+1)%5;
					
				}else {
					temp=c1;
					c1=c2;
					c2=temp;
				}
				enc[t++]=arr[r1][c1];
				enc[t++]=arr[r2][c2];
			}
		}
		if(strlen(string)%2!=0) 
		enc[t++]=string[var];
		enc[t]='\0';
	}
	printf("The encrypted text is\n");
	puts(enc);


	 t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
 
    printf("encription took %f seconds to execute \n", time_taken);
	
}

