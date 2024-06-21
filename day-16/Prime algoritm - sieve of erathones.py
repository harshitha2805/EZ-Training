def isprime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count+=1
            break 
    if count==1:
        return 1
    else:
        return 0
def fact(num,n,l):
    for i in range(num+1,n+1):
        if i%num==0:
            l[i]=False
    
n=int(input())
l=[True]*(n+1)
for i in range(2,n+1):
    if isprime(i):
        res=fact(i,n,l)
for i in range(2,n+1):
    if l[i]:
        print(i)
print(l)
        

    