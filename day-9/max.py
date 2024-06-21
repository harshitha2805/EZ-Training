def maxi(l,si,ei):
    if si==ei:
        return l[si]
    mid=(si+ei)//2
    #return max(maxi(l,si,mid),maxi(l,mid+1,ei))
    return maxi(l,si,mid) if (maxi(l,si,mid)>maxi(l,mid+1,ei)) else maxi(l,mid+1,ei)
l=list(map(int,input().split()))
print(maxi(l,0,len(l)-1))