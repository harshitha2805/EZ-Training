def bs(l,target):
    def bsc(si,ei):
        if si<=ei:
            mid=(si+ei)//2
            if l[mid]==target:
                return l[mid]
            if l[mid]<target:
                return bsc(mid+1,ei)
            return bsc(si,mid-1)
        if target>l[len(l)-1]:
            return float('inf')
        return l[si]
    return bsc(0,len(l)-1)


l=list(map(int,input().split()))
target=int(input())
print(bs(l,target))