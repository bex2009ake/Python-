# list = []

# while True:
#     a = int(input('Number: '))
#     if a == 0:
#         break
#     else:
#         list.append(a)

# print(sum(list))

# i = 1
# Sum = 0

# num = int(input('Num: '))

# while i != num:
#     i += 1
#     if '3' in str(i):
#         Sum += 1

# print(Sum)

# # ===========

# from random import randint


# randomNUM = randint(1,10)


# while True:
#     a = int(input(':'))

#     if a == randomNUM:
#         print(True)
#         break
#     elif a > randomNUM:
#         print('Big')
#     elif a < randomNUM:
#         print('Small')

a = 0 
b = int(input('Num: '))


while a != b:
    a += 1
    if b % a == 0:
        print(a)