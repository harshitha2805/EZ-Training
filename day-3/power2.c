#include<stdio.h>
/*int main()
{
	int n,a,i=0;
	printf("Enter the number:");
	scanf("%d",&n);
	while(1)
	{
		a=2<<i;
		if(a==n)
		{
			printf("%d is a power of 2",n);	
			break;
		}
		else if(a>n)
		{
			printf("Not a power of 2");
			break;
		}
		i++;
	}
	

}*/
int main()
{
	int count=0,n;
	scanf("%d",&n);
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	{
		printf("true");
	}
	else
	{
		printf("false");
	}
}