" - 1 - "

# EvenOdd = lambda num: ['Четный','Нечетный'][num % 2]
# print(EvenOdd(30))

" - 2 - "

# def Sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             sum += arr[i]
#     return sum


# print(Sum([12, 3, 4, 23, 1, 13, 6]))


" - 3 - "

# def five(arr):
#     return arr.index(5)

# print(five([1, 3, 5, 2, 8, 9]))


" - 4 - "


# def show(index):
#     a = (1,True,0,False,'Hello',None)
#     print(a[index])

# show(int(input('Index: ')))


" - 5 - "


# def List():
#     list = {}
#     num = int(input('Num of list: '))
#     for i in range(1,num+1):
#         key = input(f'Name-{i}: ')
#         value = input(f'Kind-{i}: ')
#         list[key] = value
#     print(list)

# List()


" - 6 - "

# def seven(num):
#     if 1 == num:
#         return 1
#     else:
#        return num + seven(num-1)

# print(seven(7))


# matrix = [[1,1,1],[1,0,1],[1,1,1]]

# a = []
# b = []

# for i in matrix:
#     print(i)
#     for j in range(len(i)):
#         if i[j] == 0:
#             b.append(j)

# for i in range(len(matrix)):
#     if 0 in matrix[i]:
#         a.append(i)
#         b.append(matrix[i].index(0))
# for i in a:
#     for j in range(len(matrix[i])):
#         matrix[i][j] = 0


# for i in b:
#     for j in range(len(matrix)):
#         matrix[j][i] = 0


# print(matrix)        

# nums = [5,7,7,8,8,10]
# target = 8
# a = [i for i in range(len(nums)) if nums[i] == target]
# print([a[0],a[-1]])

nums = [2,2,3,2]

print(*[i for i in nums if nums.count(i) == 1])