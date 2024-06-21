#to print a value in middle of string
'''
for i in range(10):
    print("hi",i,"hello")
    
#string formating:
    print(f"hi {i**2} hello")
#sep=","-can be used only inside
'''
#print 2D list
'''
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
o/p:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''
#print pattern
'''
for i in range(5):
    print("* "*(i+1))
o/p:
* 
* * 
* * * 
* * * * 
* * * * *
'''
#range function:returns collection of objects
'''
a=range(1,10,2)
print(a,type(a))
print(list(a))
o/p:range(1, 10, 2) <class 'range'>
[1, 3, 5, 7, 9]
'''
#str concanct:
'''
s='abs'+'d'
print(s)
*-repeating
o/p:abcd
'''
'''
#list elements to integer
def fun(a):
    return a*a
l=[2,3,4,5]
#l=map(int,input(),split())
l=list(map(fun,l))
print(l)
#o/p:[4, 9, 16, 25]
def fun(a):
    return str(a)
l=[2,3,4,5]

l=list(map(fun,l))
print(l)
#o/p:['2', '3', '4', '5']
def fun(a):
    return sum(a)
l=[[2,3,4],[5,6,7],[1,9,0]]

l=list(map(fun,l))
print(l)
#o/p:[9, 18, 10]
'''
'''
l=[[2,3,4],[5,1,7],[1,9,0]]

l=list(map(lambda a:max(a),l))
print(l)
#l=list(map(lambda a:sum(a),l))
#print(l)
l=list(map(lambda a:sorted(a),l))
print(l)
#o/p:[4, 7, 9]
'''
#filter:true-element inserted, if not-no
l=[[2,3,4],[5,1,7],[1,9,0]]
a=[2,5,4,3,8]
l=list(filter(lambda a:a%2==0,a))
print(l)
#o/p:[2, 4, 8]

l=[[1,2,3],[5,1,7],[1,9,0]]
a=[2,5,4,3,8]
l=list(filter(lambda a:a%2==0,a))
print(l)