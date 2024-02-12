" - 1 - "
# a,b = [],[]


# while True:
#     num = int(input('Num: '))
#     if num == 0:
#         print(f'{a} \n{b}')
#         break
#     else:
#         if num % 2 == 0:
#             a.append(num)
#         else:
#             b.append(num)

" - 2 - "

# three,seven = [],[]


# while True:
#     num = int(input('Num: '))
#     if num == 0:
#         print(f'3:{three} \n7:{seven}')
#         break
#     else:
#         if num % 3 == 0:
#             three.append(num)
#         if num % 7 == 0:
#             seven.append(num)


" - 3 - "

# list = []
# did = []

# while True:
#     work = input('Work: ')
#     if work == 'Stop':
#         for i in range(len(list)):
#             print(f'{i+1}-{list[i]}')
#         while True:
#             delW = input('Delet work: ')
#             if delW == 'Stop':
#                 for j in range(len(did)):
#                     print(f'Delated work: {did[j]}')
#                 break
#             else:
#                 did.append(delW)
#                 list.remove(delW)
#         break
#     else:
#         list.append(work)


" - 4 - "

# Num = []


# while True:
#     sum = 0
#     num = int(input('Num: '))
#     if num == 0:
#         print(Num)
#         break
#     else:
#         for i in range(1,num+1):
#            if num % i == 0:
#                sum += 1
#         if sum == 2:
#             Num.append(num)



"pythontutor"

" - 1 - "

nums = list(map(int,input('Nums:').split()))
copy = nums.copy()

# for i in nums:
#     copy.append(i)
#     if i in copy:
#         print(f'{i} - YES')
#     else:
#         print(f'{i}-NO')
#     nums.remove(i)


for i in nums:
    copy.remove(i)
    if i in copy:
        print(f'{i} - YES')
    else:
        print(f'{i} - NO')
        