# # 8
# num = input('Num: ')

# num = list(num)
# num[:] = list(map(int, num))

# num = str(sum(num))



# print(int(num[0])+int(num[1]))

# 5

# a = int(input('First: '))
# b = int(input('Second: '))

# i = 0

# while i != max(a,b):
#     i += 1
#     if a%i == 0 and b%i == 0:
#         print(i)


i = 0
son = int(input("Num: "))
a = []
b = []
while i != son:
    i += 1
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)

print(a,b)