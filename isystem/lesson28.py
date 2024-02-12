# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def isEmpty(self):
#         return len(self.stack) == 0
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if not self.isEmpty():
#             ...




# func = lambda a,b: 1 if str(a) in b else False
# print(func(a=int(input()),b=input().split()))


def func(a,b):
    b = list(b)
    c = 0
    if a in b:
        a = b.index(a)
        for i in b[a::]:
            if i == ' ':
                break
            else:
                c += 1
    return(c)

def countSeniors(details) -> int:
        return len([int(i[0:2]) for i in details if int(i[0:2]) > 59])

def separateDigits(nums):
        return [int(j) for i in nums for j in str(i)]

def maxSubsequence(nums,k):
        a = []
        for i in range(k):
            a.append(max(nums))
            list(nums).remove(max(nums))
        return a


# Python code to demonstrate Implementing 
# Queue using deque 
from collections import deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) 
queue.append("Akbar") 
print(queue) 
queue.append("Birbal") 
print(queue) 
print(queue.popleft())				 
print(queue.popleft())				 
print(queue) 
