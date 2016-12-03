#include<stdio.h>
#include <time.h>


int  main()
{
    int i,j,ans[25][1],sum=0,mtrx[3][3]={{17, 17,5}, {21,18,21}, {2,2,19} },end;
    char txt[25]="pay";
     clock_t t;
    t = clock();
    //printf("\nEnter the string : ");
    //scanf("%s",txt);
    end=3;
    for(i=0;i<end;i++)
    {

        //printf("initial : %d ",txt[i]);
        txt[i]=txt[i]-'a';
        //printf("final : %d ",txt[i]);
        //printf("\n\n");
    }
    printf("\nEnter matrix...\n");
   
    for(i=0;i<end;i++)
    {
        printf("\n");
        for(j=0;j<end;j++)
        {
            printf("%d ",mtrx[i][j]);
        }
    }

    for(i=0;i<end;i++)
    {
        sum=0;
        for(j=0;j<end;j++)
        {
            sum+=mtrx[i][j]*(int)txt[j];
        }
        ans[i][0]=sum;
    }
    printf("\n");
    for(i=0;i<end;i++)
    {
        printf("%c",((ans[i][0])%26)+97);
    }
     t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
 
    printf("encription took %f seconds to execute \n", time_taken);
   return 0;
}