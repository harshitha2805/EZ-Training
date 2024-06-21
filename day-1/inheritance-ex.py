#heirarchial class,multilevel,single
class Siva:
    def gold(wgl):
        print("Hello")
class Baby1(Siva):
    def bank(wgl):
        print("dep 2L")
class Baby2(Siva):
    def jewels(wgl):
        print("Diamond")
class Gbaby(Baby1):
    def grand(wgl):
        print("grand child")
b1=Gbaby()
b1.grand()
b1.bank()
b2=Baby2()
b2.jewels()
b2.gold()