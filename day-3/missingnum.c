#include<stdio.h>
int main()
{
	int n,i;
	printf("Enter n:");
	scanf("%d",&n);
	int a[n];
	printf("\nEnter %d elements:",n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	int x=0;
	for(i=0;i<=n;i++)
	{
		x=x^i;
	}
	for(i=0;i<n-1;i++)
	{
		x=x^a[i];
	}
	printf("%d",x);
}