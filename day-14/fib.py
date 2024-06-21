def fib(n,dp):
    if dp[n]:
        return dp[n]
    if n==0:
        dp[0]=0
        return 0
    if n==1:
        dp[1]=1
        return 1
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]
    
n=int(input())
dp=[0]*(n+1)
fib(n,dp)
print(dp)
print(dp[n])

