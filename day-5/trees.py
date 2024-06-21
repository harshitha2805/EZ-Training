def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
        
    if i<n-1:
        fun(l,i+1,j,n)
    if i>0:
        fun(l,i-1,j,n)
    if j<n-1:
        fun(l,i,j+1,n)
    if j>0:
        fun(l,i,j-1,n)
    
    
    
l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
fun(l,0,0,n)

for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c+=1
print(c)

'''
i/p
4
1 0 0 1
1 0 0 0
1 0 1 0
0 1 1 1
o/p
5'''