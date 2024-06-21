'''
l=list(map(int,input().split()))
for i in range(len(l)):
    print('x'*l[i])
'''
l=list(map(int,input().split()))
n=len(l)
mxm=max(l)
for i in range(mxm,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print("x",end=' ')
        else:
            print(" ",end=" ")
    print()

        