#magical prime: number prime, reverse of a number also prime ex:17=71->prime
#neon number:square number sum of digits = number ex:9^2=81=8+1=9
class Siva:
    def wel(fun):
        print("Welcome to the program")
class Baby1:
    def mag_pri(fun,n):
        temp=n
        rev=0
        flag=0
        while n>0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        for i in range(2,rev):
            if(rev%i==0):
                flag=1
                break
        if(flag==1):
            print("It is not a magical prime")
        else:
            print("It is a magical prime")          
class Baby2:
    def neon_num(fun,num):
       for i in range(0,num+1):
           sq=i*i
           sum=0
           if(sq>9):
               
               while sq>0:
                  rem=sq%10
                  sum=sum+rem
                  sq=sq//10
               if(sum==i):
                    print(i)
           else:
                sum=sq
                if(sum==i):
                    print(i)
                
           
b1=Baby1()
n=int(input("Enter the prime number:"))
b1.mag_pri(n);
b2=Baby2()
num=int(input("Enter the range to find neon numbers in between:"))
b2.neon_num(num)