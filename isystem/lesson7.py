# a = []
# b = int(input('Num: '))
# for i in range(b-1):
#     if b % (i+1) == 0:
#         a.append(i+1)
# print(max(a))



# func = lambda num : 'YES' if num % 2 == 0 else 'NO'

# print(func(90)) 


for i in range(1,10):
    print(' '*(10-i),' *'*(i),' '*(10-i))
for i in range(1,10+1):
    print(' '*(10+i-10-1),' *'*(1+10-i),' '*(10+i-10-1))