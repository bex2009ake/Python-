import random
import math 

# start

a = [1,2,3,
     4,5,6,
     7,8,9]
b = []
sum = 0
while True:
  random.shuffle(a)
  if a[0]+a[1]+a[2] == 15 and a[3]+a[4]+a[5] == 15 and a[6]+a[7]+a[8] == 15 and a[0]+a[3]+a[6] == 15 and a[1]+a[4]+a[7] == 15  and a[2]+a[5]+a[8] == 15 and a[0]+a[4]+a[8] == 15 and a[2]+a[4]+a[6] == 15:
    print(a[0],a[1],a[2])
    print(a[3],a[4],a[5])
    print(a[6],a[7],a[8])
    break
 



# def func(num):
#     a = []
#     d = []
#     b = list(str(num))
#     c = ''
#     e = ''

#     for i in b:
#         if i != '.':
#             a.append(i)
#         else:
#             break
#     for i in b[::-1]:
#         if i != '.':
#             d.append(i)
#         else:
#             break

#     for i in a:
#         c += i
#     for i in d:
#         e += i
    
#     if e[0] in ['5','6','7','8','9']:
#         print(int(c)+1)
#     else:
#         print(c)


# func(float(input('Num: ')))


# import datetime as dt

# print(dt.date.today().month)
