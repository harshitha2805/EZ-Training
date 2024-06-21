//print lonely integers in an array using bitwise
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
	int res=0;
	for(i=0;i<n;i++)
	{
		res=res^a[i];
	}
	printf("%d",res);
	
}