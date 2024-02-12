class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return f'"{self.data}" -> {self.next}'


class List:
    def __init__(self):
        self.head = None
    def all(self):
        t = self.head
        c = 0
        while t:
            t = t.next
            c += 1
        return c
    def push(self,new):
        new = Node(new)
        new.next = self.head
        self.head = new
    def delt(self):
        self.head = self.head.next
    def append(self,new):
        new = Node(new)
        if self.head is None:
            self.head = new
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new
    def add(self,*name):
      for i in name:
        i = Node(i)    
        last = self.head
        while last.next:
            last = last.next
        last.next = i
    def __str__(self):
        return str(self.head)
    

l = List()
l.head = Node(0)


# l.add('Dushanba','Seshanba','Chorshanba')
l.add(1,2,2,1)
temp = l.head
a = []
while temp.next:
    temp = temp.next
    a.append(temp.data)

print(a)
