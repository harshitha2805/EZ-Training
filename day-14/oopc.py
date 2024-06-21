#single inheritence
class engr:
    def fun1(self,a):
        print("fun1",a)
class cse(engr): 
    def fun2(self):
        super().fun1(2)
        print("fun2")
class ece():
    def fun3(self):
        print("fun3")
a=cse()
a.fun2()


