def sum1(l,si,ei):
    if si==ei:
        return l[si]
    mid=(si+ei)//2
    return sum1(l,si,mid)+sum1(l,mid+1,ei)
l=list(map(int,input().split()))
print(sum1(l,0,len(l)-1))
    