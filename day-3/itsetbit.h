//set ith bit is 1 or not, ith bit from right
#include<stdio.h>
int main()
{
	int n,pos;
	printf("Enter the number:");
	scanf("%d",&n);
	printf("\nEnter the position:");
	scanf("%d",&pos);
	if(n&1<<(pos-1))
	{
		printf("yes");
	}
	else
	{
		printf("No");
	}
	
}