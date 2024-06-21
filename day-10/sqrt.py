def sqrt_bs(number,epsilon=1e-6):
    if number<0:
        raise ValueError("Cannot compute the square root")
    if number<1:
        left,right=number, 1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_squared=mid*mid
        if mid_squared<number:
            left=mid
        else:
            right=mid
    return (left+right)/2

number=int(input())
res=sqrt_bs(number)
print(f"the square root of {number} is approximately equal to {res}")