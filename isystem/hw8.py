# #  1

# def func(a):
#     if a <= 0:
#         return
#     else:
#         func(a-1)
#         if a % 2 == 0:
#             print(a)

# func(int(input(': ')))


# 2

# import random

# num = random.randint(1,10)

# def func():
#     a = int(input())
#     if a == num:
#         print("OK")
#     else:
#         if a > num:
#             print('>')
#             return func()
#         elif a < num:
#             print('<')
#             return func()

# func()


# 3


# def func(a,b,c):
#     if a <= 0:
#         return
#     else:
#         func(a-1,b,c)

#         if b % a == 0 and c % a == 0:
#             print(a)

# one,two = int(input('1: ')),int(input('2: '))

# func(min(one,two),one,two)

# for i in range(1,10):
#     print(' '*(10-i),' *'*(i),' '*(10-i))
# for i in range(1,10+1):
#     print(' '*(10+i-10-1),' *'*(1+10-i),' '*(10+i-10-1))

# 4

# def func(a):
#     if a <= 0:
#         return
#     else:
#         func(a-1)
#         if '3' in str(a):
#             print(a)

# func(int(input(': ')))


# 5

def func(a):
    a=str(a)
    if str(a) == 'stop':
        print('Stop')
    else:
        if a != a.upper():
            print(a.upper())
            func(a)
        elif a != a.lower():
            print(a.lower())
            func(a)
        else:
            print(None)
            func(a)
func(input(': '))