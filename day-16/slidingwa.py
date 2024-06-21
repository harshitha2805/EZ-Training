def swa(l,target):
    i=0
    j=0
    sum1=l[0]
    res=[l[0]]
    while j<len(l)-1: 
            if sum1==target:
                return res
                break
            elif sum1>target: 
                sum1-=l[i]
                res.remove(l[i])
                i+=1
            else:
                j+=1
                sum1+=l[j]
                res.append(l[j])            
    return -1
l=list(map(int,input().split()))
target=int(input())
print(swa(l,target))