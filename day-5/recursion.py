'''
n=int(input())
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    
fun(n)
'''
'''
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
n=int(input())
fun(n)
''' '''
def fun(n,i):
    
    if i>10:
        return
    print(n*i)
    fun(n,i+1)
n=int(input())
i=1
fun(n,i)'''
'''
def fun(n):
    
    if(n<=1):
       return n
    else:
       return n+fun(n-1)
   
n=int(input())
print(fun(n))'''
 '''   
s=input()
i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("Not palindrome")
        break
    i=i+1
    j=j-1
else:
    print("palindrome")
'''

def palin(s,i,j):
    if(i<j):
        if(s[i]!=s[j]):
            print("Not palindrome")
            return
        else:
            palin(s,i+1,j-1)
    else:
        print("Palindrome")
       
s=input()
i=0
j=len(s)-1
palin(s,i,j)



    