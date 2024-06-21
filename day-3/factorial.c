#include<stdio.h>
long long int fact(long long int n)
{
	if(n==1||n==0)
	{
		return 1;
	}
	else
	{
		return n*fact(n-1);
	}
}
int main()
{
	long long int n,f;
	printf("\nEnter the number:");
	scanf("%lld",&n);
	f=fact(n);
	printf("factorial=%lld",f);
}