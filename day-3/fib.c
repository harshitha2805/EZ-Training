#include<stdio.h>
/*int fib(int n)
{
	if(n==0||n==1)
	{
		return n;
	}
	else
	{
		return fib(n-1)+fib(n-2);
	}
}
int main()
{
	int n,i;
	printf("Enter n value:");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("%d ",fib(i));
	}
}
*/
int main()
{
	int n,i;
	printf("Enter n value:");
	scanf("%d",&n);
	long long int f1=0,f2=1,f3;
	printf("%lld %lld",f1,f2);
	for(i=2;i<n;i++)
	{
		f3=f1+f2;
		printf(" %lld",f3);
		f1=f2;
		f2=f3;
	}
}
