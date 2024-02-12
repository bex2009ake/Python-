# a = [[1,2,3],[4,5,6],[7,8,9]]

# sum = 0

# for i in range(len(a)):
#     sum += a[i][i]

# print(sum)

# list = []

# while True:
#     num = int(input('Num: '))
#     if num == 0:
#         for i in list:
#             if i % 2 == 0:
#                 print(f'{i} ',end='')
#         break
#     else:
#         list.append(num)


# list = [1,2,3,4,5,6,7,8,9,10,11,22,33,55,6,788,76,43365,67,3234,0]

# for i in list:
#     if i > 9 and i < 100:
#         print(i)



# a = [3,5,7,9]

# for i in a:
#     print(f'{i}:{"*"*i}')

# a = [1,1,1,2,2,3,3,3,3,7,7]
# b = set(a.copy())

# for i in b:
#     print(f'{i}: {"*"*a.count(i)}')

a = [1,1,1,2,2,3,3,3,3,7,7]

for i in range(len(a)):
    for i in a:
        if i == a[i]:
          print(i,'*'*a[i])