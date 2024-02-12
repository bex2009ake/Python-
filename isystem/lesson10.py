# list = [3,7,2,7]
# a = 5

# for i in range(len(list)):
#     for j in range(i,len(list)):
#         if list[i]+list[j] == a:
#             print(i,j)

# list = [5,4,3,2,1]


# for i in range(len(list)):
#     for j in range(i,len(list)):
#         if list[i] >= list[j]:
#             list[i],list[j] = list[j],list[i]

# print(list)


list = [5,4,3,2,1]
a = []

for i in range(len(list)):
    a.append(min(list))
    list.remove(min(list))

print(a)