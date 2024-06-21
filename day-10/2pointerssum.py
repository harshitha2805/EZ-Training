l=list(map(int,input().split()))
n=len(l)
target=int(input())
left=0
right=n-1
while left<right:
    sum1=l[left]+l[right]
    if sum1==target:
        print(f"{l[left]},{l[right]} gives the sum {target}")
        break
    elif sum1<target:
        left+=1
    else:
        right-=1

 