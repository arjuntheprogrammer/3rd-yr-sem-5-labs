#include<stdio.h>
#include<string.h>
#include <time.h>

int main()
{
int lk,i,j,k,l,m;
char a[20],c[20],d[20];
int key[3]={1,2,3};

 clock_t t;
    t = clock();

printf("\nEnter the input string : ");
scanf("%s",a );
l=strlen(a);

j=0;
/*Ciphering*/
for ( m = 0; m < 3; ++m)
{
	printf("here\n");
	if(key[m]==1)
		for(i=0;i<l;i++)
		{

		if(i%3==0){

		c[j++]=a[i];}
		}
		

	else if(key[m]==2)
		for(i=0;i<l;i++)
		{

		if(i%3==1){

		c[j++]=a[i];}
		}
	
	else if(key[m]==3)
		for(i=0;i<l;i++)
		{

		if(i%3==2){

		c[j++]=a[i];}
		}
		   

}

printf("\nCipher text after applying rail fence :");

for (i = 0; i < l; ++i)
{
	printf("%c", c[i]);
}

printf("\n");
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
 
    printf("encription took %f seconds to execute \n", time_taken);
return 0;
}