# a ={1,2,3,4,8}
# b ={5,6,7,8}

# print(a.union(b))

# x = int(input(': '))


# x = list(str(x))
# if x == x[::-1]:
#     print(True)
# else:
#     print(False)

# nums = [2,7,11,15]
# target = 9

# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i,j])


# a = int(input())

# if a // 60 == 24:
#     print(0,a % 60)
# if a // 60 > 25:
#     b = a // 60
#     while b > 24:
#         b -= 24
#     print(b,a % 60)
# if a // 60 < 24:
#     print(a // 60,a % 60)


# a = input().split()
# a = list(map(int,a))
# x = int(input())

# for i in range(1,len(a)):
#     # for j in range(i,len(a)):
#         if x < min(a):
#             print(len(a)+1)
#             break
#         if x > max(a):
#             print(1)
#             break
#         if x < a[i] and x > a[i+1]:
#             print(i-1) 
#             break




a = int(input('Rows: '))

for i in range(1,a):
    print(' '*(a-i),' *'*i,' '*(a-i))


for i in range(1,a+1):
    print(' '*(a+i-a-1),' *'*(1+a-i),' '*(a+i-a-1))