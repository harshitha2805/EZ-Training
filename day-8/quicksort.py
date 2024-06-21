def quick(l,start,end):
    if start<end:
        pi=qsort(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)
    
def qsort(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[j],l[i]=l[i],l[j]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

    l=list(map(int,input().split()))
n=len(l)
quick(l,0,n-1)
for i in range(n):
    print(l[i],end=' ')

    