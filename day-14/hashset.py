class MyHashSet:

    def __init__(self):
        self.s=set()
        

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.s:
            return True
        else:
            return False
obj = MyHashSet()
obj.add(20)
obj.add(800)
obj.remove(20)
param_3 = obj.contains(800)
print(param_3)