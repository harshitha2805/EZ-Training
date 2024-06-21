class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
         
    def deleteend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next

    def revprint(self):
        hp=self.head
        while(hp):
            hp.prev,hp.next=hp.next,hp.prev
            hp=hp.prev
        self.head,self.tail=self.tail,self.head
        
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,7,9]
m=[5,1,3,8]
o=dll()
for i in m:
    o.insertatbeg(i)
o.printing()
print()
for j in l:
    o.insertatend(j)
o.printing()
print()
o.deleteatbeg()

o.printing()
print()
o.deleteend()

o.printing()
print()
o.revprint()
print()
