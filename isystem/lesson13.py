nechi = int(input("Nechtalik: "))
a = []
for i in range(nechi):
    a.append([int(i) for i in input(f"{i+1}-qator: ").split()])
print(a)

sum = 0

for i in range(len(a)):
    sum += a[i][-(i+1)]
print(sum)

sum = 0

for i in range(len(a)):
    sum += a[i][i]
print(sum)

sum = 0

for i in range(len(a)):
    for j in range(len(a)):
            sum += a[i][j] 
print(sum)
