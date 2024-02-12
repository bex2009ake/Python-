" -1- : Написать программу, которая вычисляет сумму двух чисел"

# a,b = int(input("First num:")),int(input("Second num:"))

# print(f'Answer: {a+b}')



" -2- Распечатайте прямоугольник по номеру."

# print("222222\n2    2\n2    2\n222222")



" -3- напечатайте треугольник через букву."

# print("  A\n A A\nAAAAA")


" -5- Распечатайте котенка, как показано в примере."

# print("\    /\\\n )  ( ')\n(  /  )\n \(__)|")


" -6- Распечатайте щенка, как показано в примере."

# print('|\_/|\n|qp| /}\n( 0 )"""\\\n|"^"` |\n||_/=\\\__|')


" -7- Прочитайте 2 числа, обозначающие дату рождения. Первая цифра обозначает oy, а вторая kunобозначает . Распечатайте дату рождения, как показано на рисунке."

# a = input("Data:").split()

# if int(a[0]) < 10:
#    a[0] = "0" + str(a[0])
   
# if int(a[1]) < 10:
#    a[1] = "0" + str(a[1]) 

# print(f'Birthday is {a[0]}-{a[1]}.')


" -8- N прочитайте число и N напечатайте квадрат через это."

# num = input("Enter num:")

# print(f'{num+num+num+num+num+num}\n{num}    {num}\n{num}    {num}\n{num+num+num+num+num+num}')


" -10- N Распечатайте таблицу умножения числа"

# def math():
#     a = int(input("Number:"))
#     if a > 1 and a < 10:
#        print(f"""
# {a}*1={1*a}
# {a}*2={2*a}
# {a}*3={3*a}
# {a}*4={4*a}
# {a}*5={5*a}
# {a}*6={6*a}
# {a}*7={7*a}
# {a}*8={8*a}
# {a}*9={9*a}
#       """)
#     else:
#         print("Your number have to be little than 10 and more than 1")

# try:
#     math()

# except:
#     print("You have to write only numbers")


" -4- Выведите сумму чисел до 5 faktorial"


# print("1!=",1)
# print("2!=",1*2)
# print("3!=",1*2*3)
# print("4!=",1*2*3*4)
# print("5!=",1*2*3*4*5)