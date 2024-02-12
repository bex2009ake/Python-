# misol - 1


a = input('Name: ')
b = input('Surname: ')

print(f'Name: {a} \nSurname:{b}')

# misol - 2
num = int(input('Any num: '))


for i in range(1,9):
    print(' '*(9-i),f' {num}'*i,' '*(9-i))
print(' '*8,'||')


# misol - 3

sum = 0

for i in range(10):
    a = int(input(f'Num-{i+1}: '))
    if a > 9 and a < 100:
       sum += a

print(sum)


# misol - 4

numOne = int(input('Num one: '))
numTwo = int(input('Num two: '))


for i in range(numOne,numTwo+1):
    if i % 3 == 0:
        print(i)

# misol - 5

num = int(input('Num: '))

sum = 0

for i in range(1,num+1):
    if i % 2 == 0:
        sum += pow(i,2)

print(sum)

# misol - 6

num = int(input('Num: '))

if num > 9 and num < 100 and num % 2 != 0:
    print(num)
else:
    print(None)

# misol - 7

all = 0

while True:
    sum = 0
    a = int(input('Num: '))
    if a == 0:
        break
    for i in range(a):
        if a % (i+1) == 0 and a % 1 == 0:
            sum += 1
    if sum == 2:
        all += a



        
print(all+1)