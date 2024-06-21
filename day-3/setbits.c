#include<stdio.h>
int main()
{
	long int a;
	int count=0;
	printf("Enter the number:");
	scanf("%ld",&a);
	while(a)
	{
		count++;
		a=a&(a-1);
	}
	printf("%d",count);
	/*
	while(a>0)
	{
	if(a&1)
	{
	count++;
    }
    a=a>>1;
    }
	*/
}