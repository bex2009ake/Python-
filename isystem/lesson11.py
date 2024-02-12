# nums = set()

# while True:
#     num = int(input('Num: '))
#     sum = 0
#     if num == 0:
#         break
#     else:
#         for i in range(1,num+1):
#             if num % i == 0:
#                 sum += 1
#         if sum == 2:
#             nums.add(num)
# print(nums)



a = [1,2,3,4,5,6]

for i in range(len(a)):
    for j in range(len(a)):
        for z in range(len(a)):
            if a[i] + a[j] + a[z] == 10:
                if a[i] != a[j] and a[i] != a[z] and a[j] != a[z]:
                       print(a[z],a[j],a[i])


print(9999999+9999)