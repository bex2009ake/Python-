# def sayHello(name):
#     print('Hello',name)
# sayHello('Behruz')

# class Func:
#     def __init__(self,name) -> None:
#         self.name = name
#     def sayHello(self):
#         print('Hello',self.name)

# Func('Fazliddin').sayHello()


# import collections

# a = collections.deque([1,2,3,4,5])
# a.appendleft(0)
# for i in a:
#     print(i)


# print(sorted([int(i) for i in input().split()],reverse=True)[0:2])

# a = list(map(int,input().split()))
# a = [5,4,3,2,1]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j] = a[j],[i]



# print(a)

import queue


# q = queue.Queue()
# for i in range(1,11):
#     q.put(i)
# print(q.get())


# ql = queue.LifoQueue()

# for i in range(1,11):
#     ql.put(i)

# while not ql.empty():
#  print(ql.get())


# qp = queue.PriorityQueue()

# qp.put((3,4))
# qp.put((5,6))
# qp.put((7,8))
# qp.put((1,2))
# print(qp.queue)


import requests
from bs4 import BeautifulSoup



url = requests.get('https://dev.vk.com/ru/reference/json-schema')
bs = BeautifulSoup(url.text,'html.text')

print(url)