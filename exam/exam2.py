# def longestConsecutive(nums) -> int:
#         if len(nums) == 0:
#             return 0
#         a = list(set(nums))
#         a.sort()

#         s = 0


#         for i in range(len(a)):
#             if not i == (len(a)-1):
#                 if a[i+1] - a[i] == 1:
#                     print(a[i])
#                     print(a[i+1],'-',a[i])
#                     s += 1


# # 128
# print(longestConsecutive([100,4,200,1,3,2]))


a = 321

print(hex(a))