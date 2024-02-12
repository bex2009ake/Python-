# def func(a):
#     if a == 2:
#         return 2
#     else:
#      return a + func(a - 2) 

# a = int(input(':'))

# if a % 2 == 0:
#   print(func(a))
# else:
#   print(func(a-1))



# dekarator


def func(n,a):
    s = 0
    if n <= 0:
        return
    else:
        func(n-1,a)
        if a % n == 0:
            print(n)

func(7,7)