#include<stdio.h>
int main()
{
	int lemon,req_lemons;
	printf("\nEnter the number of lemons u have:");
	((scanf("%d",&lemon)==1))?((lemon==0)?printf("Enter valid integer type"):((lemon<0)?printf("Not valid, enter valid input"):((lemon>21)?printf("%d lemons are extra",lemon-21):printf("Required lemons=%d",21-lemon)))):(printf("Enter in int datatype"));
}