#include<stdio.h>
int main()
{
	int n;
	printf("Enter size of matrix:");
	scanf("%d",&n);
	int a[n][n],i,j,zrc[n],orc[n],zldc=0,oldc=0,zrdc=0,ordc=0,zcc[n],occ[n];
	printf("\nEnter 0's and 1's randomly for a 4x4 matrix");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(i=0;i<n;i++)
	{
		zrc[i]=0;
		orc[i]=0;
		for(j=0;j<n;j++)
		{
			if(a[i][j]==0)
			{
				zrc[i]++;	
			}
			else if(a[i][j]==1)
			{
				orc[i]++;
			}
		}
		
	}
	for(i=0;i<n;i++)
	{
	
		for(j=0;j<n;j++)
		{
			if(i==j)
			{
				if(a[i][j]==0)
				{
					zldc++;
				}
				else if(a[i][j]==1)
				{
					oldc++;
				}
			}	
		}	
	}
	for(i=0;i<n;i++)
	{
		
		for(j=n-1;j>=0;j--)
		{
		
			if(j+i==n-1)
			{
			
				if(a[i][j]==0)
				{
					zrdc++;
				}
				else if(a[i][j]==1)
				{
					ordc++;
				}
			}		
		}	
	}
	for(i=0;i<n;i++)
	{
		zcc[i]=0;
		occ[i]=0;
		for(j=0;j<n;j++)
		{
			if(a[j][i]==0)
			{
				zcc[i]++;	
			}
			else if(a[j][i]==1)
			{
				occ[i]++;
			}
		}	
	}
/*	printf("\n");
	for(i=0;i<n;i++)
	{
	printf("%d \t",zrc[i]);
    }
    printf("\n");
    for(i=0;i<n;i++)
	{
	printf("%d \t",orc[i]);
    }
    printf("\n");
    
	printf("%d \t",zldc);
    
    printf("\n");
    
	printf("%d \t",oldc);
    
    printf("\n");
    
	printf("%d \t",zrdc);
    
    printf("\n");
   
	printf("%d \t",ordc);
    printf("\n");
	for(i=0;i<n;i++)
	{
	printf("%d \t",zcc[i]);
    }
    printf("\n");
    for(i=0;i<n;i++)
	{
	printf("%d \t",occ[i]);
    }
    */
    int morc=0,mzrc=0,mzcc=0,mocc=0,mzld=0,mold=0,mzrd=0,mord=0;
    for(i=0;i<n;i++)
    {
    	if(orc[i]==n)
    	{
    		morc++;
		}
		if(zrc[i]==n)
		{
			mzrc++;
		}
		if(zcc[i]==n)
		{
			mzcc++;
		}
		if(occ[i]==n)
		{
			mocc++;
		}
	}
	if(zldc==n)
	{
		mzld++;
	}
	if(oldc==n)
	{
		mold++;
	}
	if(zrdc==n)
	{
		mzrd++;
	}
	if(ordc==n)
	{
		mord++;
	}
	printf("\n1's horizontal count=%d",morc);
	printf("\n1's vertical count=%d",mocc);
	printf("\n1's left diagonal count=%d",mold);
	printf("\n1's right diagonal count=%d",mord);
    printf("\n0's horizontal count=%d",mzrc);
	printf("\n0's vertical count=%d",mzcc);
	printf("\n0's left diagonal count=%d",mzld);
	printf("\n0's right diagonal count=%d",mzrd);
}