# 1

# a = int(input("Num: "))

# if a < 0:
#     print('No')
# elif a >= 0 and a < 40:
#     print('Yes')
# elif a >= 40:
#     print('No')
# else:
#     print('I don`t know')



# 2

# a = int(input("Num 1: "))
# b = int(input("Num 2: "))

# if max(a,b) % min(a,b) == 0: 
#     print(f'{min(a,b)}*{int(max(a,b)/min(a,b))}={max(a,b)}')
# else:  
#     print(None)


# 3

# a = int(input("Num 1: "))
# b = int(input("Num 2: "))

# if a > b:
#     print('Num one')

# if a < b:
#     print('Num two')

# else: 
#     print('Nums equel')


# 4

# a = int(input('Num one:'))
# b = int(input('Num two:'))
# c = int(input('Num three:'))


# list = []

# list.append(a)
# list.append(b)
# list.append(c)

# Max = list[0]
# Min = list[0]
# for ele in list:
#     if ele > Max:
#         Max = ele
#     if ele < Min:
#         Min = ele


# print(Max,' ',Min)


# 5

# a = int(input("Num: "))

# if a%2 == 0 and a%3 == 0 and a%5 == 0:
#     print('All')
# elif a%2 == 0 and a%3 == 0:
#     print('Two')
# elif a%2 == 0 and a%5 == 0:
#     print('Two')
# elif a%5 == 0 and a%3 == 0:
#     print('Two')
# elif a%2 == 0 or a%3 == 0 or a%5 == 0:
#     print('One')
# else:
#     print('N')


# 6


# a = int(input())

# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('YES')
# else:
#     print('NO')


# 10

# num_one = int(input('First number: '))
# num_two = int(input('Second number: '))
# symbol = input('Symbol: ')

# match symbol:
#     case '+':
#         print(num_one+num_two)
#     case '-':
#         print(num_one-num_two)
#     case '/':
#         print(num_one/num_two)
#     case '*':
#         print(num_one*num_two)
#     case _:
#         print('Error')



# # 11

# print('Americano(￦500) 2. Caffe Latte(￦400) 3. Lemon Tea(￦300)')

# drink = input('What drink you will: ')
# money = int(input('Enter money:'))


# match drink:
#     case '1':
#         if money >= 500:
#          print(f'Americano,{money - 500}') 
#         else:
#            print('Pay more')
#     case '2':
#         if money >= 400:
#          print(f'Caffe Latte,{money - 400}') 
#         else:
#            print('Pay more')
#     case '3':
#         if money >= 300:
#          print(f'Americano,{money - 300}') 
#         else:
#            print('Pay more')
#     case _:
#       print('Error')


# 7

# a = int(input(':'))
# b = 5


# if a == b:
#     print('Correct')
# elif a < b:
#     print('UP')
# elif a > b:
#     print('DOWN')


