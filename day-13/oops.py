'''
class cse:
    def __init__(self,a):
        print("hi",a)
    def fun(self,b):
        print("hello",b)
o=cse(2)
#o.__init__(5)
o.fun(12)
'''
class cse:
    def __init__(self,a):
        self.a=a
    def fun(b):
        print("hello",b.a)
o=cse(2)
o.fun()
#o.__init__(5)