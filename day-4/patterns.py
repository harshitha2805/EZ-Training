
'''
i/p:a
o/p:1
a=input()
if(a.isupper()):  #ord(a)>96 ord(a)-96
    print(ord(a)-64)
else:
    print(ord(a)-96)
'''
'''
i/p:a 2
o/p:c
a=input()
pos=int(input())
if((ord(a)>96 and ord(a)<123) or (ord(a)>64 and ord(a)<91)):
    b=ord(a)+pos
    print(chr(b))
else:
    b=ord(a)+pos-26
    print(chr(b))
'''
'''
i/p:3
o/p:
*
* *
* * *
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("* ",end=" ")
    print("\n")
    
'''
'''
i/p:3
o/p:
  *
 * *
* * *

a=int(input())
for i in range(a):
    for j in range(a-i):
        print(" ",end='')
    for k in range(i+1):
        print("*",end=' ')
    print()'''
'''
i/p:3
o/p:
 
* * *
 * *
  * 
a=int(input())
for i in range(a):
    print(" "*(i+1)+"* "*(a-i))'''

'''
i/p:3
o/p:

  *
 * *
* * *
* * *
 * *
  * 
a=int(input())
for i in range(a):
    print(" "*(a-i)+"* "*(i+1))
for i in range(a):
    print(" "*(i+1)+"* "*(a-i))
'''
'''
i/p:4
o/p:
1
22
333
4444
a=int(input())
for i in range(a):
    print(str(i+1)*(i+1))

'''
'''
i/p:4
o/p:
1
20
300
4000
a=int(input())
for i in range(1,a+1):
    print((10**(i))*i)'''
'''
i/p:4
o/p:
1
22
333
4444

a=int(input())
for i in range(1,a+1):
    print(((10**i)//9)*i)

'''




