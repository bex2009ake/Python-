def findNthDigit(n) -> int:
        if n <= 9:
            return n
        a = [i for i in range(1,n+2)]
        b = []
        for i in a:
            if len(b) >= n:
                return int(b[n])
            else:
             for j in str(i):
                b.append(j)



print(findNthDigit(12))


# def findNthDigit(n) -> int:
#         if n <= 9:
#             return n
#         b = []
#         for i in range(1,n+2):
#             for j in str(i):
#               for j in str(i):
#                 b.append(j)
#             if len(b) >= n:
#                 return int(b[n-1])

# print(findNthDigit(11))