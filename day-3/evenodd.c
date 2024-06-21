#include<stdio.h>
int main()
{
	int a;
	printf("Enter the number:");
	scanf("%d",&a);
	if(a&1==1)  //if(a&1)
	{
		printf("odd");
	}
	else
	{
		printf("even");
	}
}