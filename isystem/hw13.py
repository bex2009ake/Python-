nechi = int(input("Nechtalik: "))
a = []
b = []
for i in range(nechi):
    a.append([int(i) for i in input(f"{i+1}-qator: ").split()])
print(a)

sum1 = 0

for i in range(len(a)):
    sum1 += a[i][-(i+1)]
    if sum1 == 15:
     b.append(sum1)
# print(sum1)

sum2 = 0

for i in range(len(a)):
    sum2 += a[i][i]
    if sum2 == 15:
     b.append(sum2)
# print(sum2)

sum3 = 0

for i in range(len(a)):
    for j in range(len(a)):
        sum3 += a[i][j] 
    if sum3 == 15:
     b.append(sum3)    
# print(sum3)


sum4 = 0

for i in range(len(a)):
    for j in range(len(a)):
        sum4 += a[j][i] 
    if sum4 == 15:
     b.append(sum4)
    
# print(sum4)

if len(b) == 4:
 print('You won !!!')
else:
   print('Looser !!!')