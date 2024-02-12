# i = 0

# sum = 1
# num = int(input('Num: '))

# while i <= num:
#     j = 0
#     sum = 1
#     while j != i:
#         j += 1
#         sum *= j

#     print(sum)
#     i += 1


# num = int(input('Num: '))

# for i in range(num):
#     sum = 1
#     for j in range(i+1):
#         sum *= j+1
#     print(f'Factorial-{i}: {sum}')


# son = int(input("Son: "))
# for j in range(2, son + 1):
#     tub = 0
#     for i in range(1, j+1):
#         if j % i == 0:
#             tub += 1
#     if tub == 2:
#         print(f"{j} - Tubson")


# a = '*'
# b = ' '


# for i in range(9):
#     for j in range(i):
#         print(b*j,str(a*j),b*j)


# yulduz = '*'
# joyt = ' '
# i = 4
# j = 1
# s = 2
# while i >= 1:
#     print(i * joyt, end='')
#     while j <= s:
#         print(j * yulduz)
#         j += 2
#     s += 2
#     i -= 1

# yulduz2 = '*'
# joyt2 = ' '
# i2 = 1
# j2 = 1
# s2 = 2
# while i2 >= 4:
#     print(i2 * joyt2, end='')
#     while j2 >= s:
#         print(j2 * yulduz)
#         j2 += 2
#     s2 -= 2
#     i2 += 1




# a = int(input('Num-1: '))
# b = int(input('Num-2: '))

# if a ** 2 == b or b ** 2 == a:
#     print(f'{int(max(a,b)/min(a,b))}*{int(max(a,b)/min(a,b))}={max(a,b)}')
# else:
#     print(None)


# a = input('Two nums: ').split()

# a = list(map(int, a))

# if a[0] ** 2 == a[1] or a[1] ** 2 == a[0]:
#     print(f'{int(max(a[0],a[1])/min(a[0],a[1]))}*{int(max(a[0],a[1])/min(a[0],a[1]))}={max(a[0],a[1])}')
# else:
#     print(None)

# a = 0


# for i in range(15):
#     i += 1
#     for j in ra

# a = int(input('Num: '))

# for i in range(1,a):
#     print(' '*(a-i),' *'*i,' '*(a-i))

# for i in range(1,a+1):
#     print(' '*(a+i-(a+1)),' *'*(1+a-i),' '*(a+i-(a+1)))


# a = int(input('Num: '))

# while True:
#     if a != 0:
#         print(['Чотный','Нечотный'][a % 2])
#         a = int(input('Num: '))
#     elif a == 0:
#         break





# for i in range(9):
#     for j in range(1,11):
#      j += i
#      if j == 10 and j < 11:
#         j = 0
#      if j > 10:
#         j = 0
#         j += i
      
#      print(j,end=' ')
     
#     print('\n')




# for i in a:
#     # a.pop(0)
#     # a.append(int(i/2))
#     # print(a)
#     print(i)
print('6-5) Problem 7')
a = [0,1,2,3,4,5,6,7,8,9]

for i in range(10):
    a.pop(0)
    a.append(int(i))
    print(a)
