import random

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return f'[{self.data}] -> {self.next}'
    
class List:
    def __init__(self):
        self.head = None
    def __str__(self):
        return str(self.head)


l = List()
n = Node(1)
l.head = n

for i in range(10):
    n.next = Node(random.choice(['a','b','c','d',True,False]))
    n = n.next
print(l)