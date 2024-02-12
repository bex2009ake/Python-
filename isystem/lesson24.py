# from abc import ABC,abstractclassmethod


# class Avto(ABC):
#     @abstractclassmethod
#     def say():
#         ...

# class Tesla(Avto):
#     def __init__(self,speed,weight,color):
#         self.speed = speed
#         self.weight = weight
#         self.color = color
#     def say(self):
#         return self.speed,self.color,self.weight
    
# a = Tesla(1200,23,'red')

# print(a.say())

# 'I', 'V', 'X', 'L', 'C', 'D', 'M'
# def romanToInt(s):
#         list(s)
#         sum = 0
#         for i in range(len(s)):
#             if s[i] == 'I':
#                 sum += 1
#             if s[i] == 'V':
#                sum += 5
#             if s[i] == 'X':
#               sum += 10
#             if s[i] == 'L':
#               sum += 50
#             if s[i] == 'C':
#               sum += 100
#             if s[i] == 'D':
#               sum += 500
#             if s[i] == 'M':
#               sum += 1000
#             if i > 0 and s[i] == 'V' and s[i-1] == 'I':
#               sum += -2
#             if i > 0 and s[i] == 'X' and s[i-1] == 'I':
#               sum += -2
#             if i > 0 and s[i] == 'C' and s[i-1] == 'X':
#               sum += -20
#             if i > 0 and s[i] == 'M' and s[i-1] == 'C':
#               sum += -200
#             if i > 0 and s[i] == 'L' and s[i-1] == 'X':
#               sum += -20
#             if i > 0 and s[i] == 'D' and s[i-1] == 'C':
#               sum += -200
#         return sum

# print(romanToInt("MCMXCIV"))
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __str__(self):
#         return f'[{self.data}] -> {self.next}'
    

# class List:
#     def __init__(self):
#         self.head = None
#     def __str__(self):
#         return str(self.head)
    
# list = List()
# node = Node(1)
# list.head = node


# for i in range(1,6):
#     node.next = Node(i)
#     node = node.next

# print(list)

print({1,2,3}.intersection({1}))