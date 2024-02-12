# - 1 -

# list = []

# while True:
#     a = int(input('Num: '))
#     if a == 0:
#         for i in list:
#           if i > 9 and i < 100:
#             print(i)
#         break
#     else:
#        list.append(a)

# - 2 -

# list = [1,2,3,4,5]
# a = list.pop(0)
# list.append(a)

# for i in list:
#     print(i,end=' ')

# - 3 -

# a = [1,1,1,2,2,3,3,3,3,7,7]
# b = set(a.copy())

# for i in b:
#     print(f'{i}: {"*"*a.count(i)}')

# # - 4 -

# list = [1,2,3,4,5]
# a = max(list)
# list.remove(a)

# print(a,max(list))


# - 5 -

# txt = 'catbcat'.split('b')
# sum = 0

# for i in txt:
#     sum += 1

# print(sum)


# - 6 -


# List = ['*','a', 'b', 'c','d']

# for i in List:
#     print((List))
#     a = List[-1]
#     List.pop(-1)
#     List.insert(0,a)


# - 7 -

# a = [[1,2,3],[4,5,6],[7,8,9]]

# sum = 0

# for i in range(len(a)):
#     sum += a[i][i]


# - 8 -

a = [0,1,2,3,4,5]


for i in a:
    match i:
        case 0:
            print('ZERO-')
        case 1:
            print('ONE--')
        case 2:
            print('TWO--')
        case 0:
            print('THREE')
        case 0:
            print('FOUR-')
        case 5:
            print('FIVE-')
