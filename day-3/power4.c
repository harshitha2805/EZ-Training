#include<stdio.h>
int main()
{
	int n,a,i=0;
	printf("Enter the number:");
	scanf("%d",&n);
	if(n==1)
	{
		printf("power of 4");
	}
	else
	{
	
	while(1)
	{
		a=4<<(i*2);
		if(a==n)
		{
			printf("%d is a power of 4",n);	
			break;
		}
		else if(a>n)
		{
		    printf("Not a power of 4");
			break;
		}
		i++;
	}
    }

}