# def sortNum(nums):
#     a = []
#     for i in list(nums):
#       a.append(max(nums))
#       nums.remove(max(nums))
#     return a


# print(sortNum([2,5,1,7,1]))


# def boblSort(num):
#     for i in range(len(list(num))):
#         for j in range(i,len(list(num))):
#             if num[i] > num[j]:
#                 num[i],num[j] = num[j],num[i]
#     return num



# print(boblSort([2,5,1,7,1]))


# from random import randrange

# def qsort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array.pop(0)
#         # pivot = array.pop(randrange(len(array)))

#         kichik = [i for i in array if i <= pivot]
#         katta = [i for i in array if i > pivot]
#         print(f"{kichik}+[{pivot}]+{katta}")
#         return qsort(kichik) + [pivot] + qsort(katta)

# array1 = [1, 5, 12, 0, -5, 66]
# print(array1)


# def reversePrefix(word: str, ch: str) -> str:
#         word = list(word)
#         for i in range(len(word)):
#             if word[i] != ' ':
#               word[word.index(ch)] = word[i]
#               break
#         for i in range(len(word)):
#             if word[i] != ' ':
#                 word[i] = ch
#                 break 
#         return ''.join(word)

# print(reversePrefix(word = " abcd efd", ch = "d"))

# def isValid(s: str) -> bool:
#         a = []
#         b = []


#         # if len(s) % 2 == 0:
#         #     return False

#         for i in s:
#             if i in '{[(':
#                 if i == '{':
#                     a.append('a')
#                 if i == '[':
#                     a.append('b')
#                 if i == '(':
#                     a.append('c')
#             if i in '}])':
#                 if i == '}':
#                     b.append('a')
#                 if i == ']':
#                     b.append('b')
#                 if i == ')':
#                     b.append('c')


#         for i in a:
#             for j in b:
#                 if a == b:
#                     a.pop(a.index(i))
#                     b.pop(b.index(j))

        
#         return False if len(a)+len(b) != 0 else True
#         # return len(a) + len(b)

# print(isValid('()[]{}'))


def plus(a,b):
    ...


def marge(num):
   if len(num) == 1:
      return 1

   mid = len(num)//2
   left = marge(num[:mid])
   right = marge(num[mid:])

   return plus(left,right)

def searchMatrix(self, matrix, target: int) -> bool:
        return target in [j for i in matrix  for j in i ]


def missingNumber(nums) -> int:
        a = set([i for i in range(len(nums)+1)]).difference(set(nums))
        for i in a:
             return i
a = [5,7,7,8,8,10]

# print([a.index(8),a.index(8)+(a[::-1]).index(8)])
set().intersection

def searchRange( nums, target: int):
        return [nums.index(target),nums.index(target)+(nums[::-1]).index(target)]


def intToRoman(num: int) -> str:
   a = []
   for i in str(num):
      a.append(i+''.join(['0' for j in range(list(num[::-1]).index(i))]))
   return a


def numIdenticalPairs(nums) -> int:
   return len([[i,j] for i in range(len(nums)) for j in range(len(nums)) if nums[i] == nums[j] and i != j])//2

a = 0
text1 = "ezupkr"
text2 = "ubmrapg"
for i in list(text1):
   if i in text2:
      a += 1
      print(i)
print(a)