from random import randint



l1 = '    '
l2 = '    '
l3 = '    '
l4 = '    '
l5 = '    '
l6 = '    '
l7 = '    '
l8 = '    '
l9 = '    '


list = []
sum = 0
mark = ''


while True:
 

 print(f"""
         1    2    3
      
    1   {l1}|{l2}|{l3}
        ____|____|____
    2   {l4}|{l5}|{l6}
        ____|____|____
    3   {l7}|{l8}|{l9}
            |    |
    """
 )

 if l1 == ' X  ' and l2 == ' X  ' and l3 == ' X  ':
  print('X won !!!')
  break
 elif l4 == ' X  ' and l5 == ' X  ' and l6 == ' X  ':
  print('X won !!!')
  break
 elif l7 == ' X  ' and l8 == ' X  ' and l9 == ' X  ':
  print('X won !!!')
  break
 elif l1 == ' X  ' and l4 == ' X  ' and l7 == ' X  ':
  print('X won !!!')
  break
 elif l2 == ' X  ' and l5 == ' X  ' and l8 == ' X  ':
  print('X won !!!')
  break
 elif l3 == ' X  ' and l6 == ' X  ' and l9 == ' X  ':
  print('X won !!!')
  break
 elif l1 == ' X  ' and l5 == ' X  ' and l9 == ' X  ':
  print('X won !!!')
  break
 elif l3 == ' X  ' and l5 == ' X  ' and l7 == ' X  ':
  print('X won !!!')
  break
 elif l1 == ' O  ' and l2 == ' O  ' and l3 == ' O  ':
  print('O won !!!')
  break
 elif l4 == ' O  ' and l5 == ' O  ' and l6 == ' O  ':
  print('O won !!!')
  break
 elif l7 == ' O  ' and l8 == ' O  ' and l9 == ' O  ':
  print('O won !!!')
  break
 elif l1 == ' O  ' and l4 == ' O  ' and l7 == ' O  ':
  print('O won !!!')
  break
 elif l2 == ' O  ' and l5 == ' O  ' and l8 == ' O  ':
  print('O won !!!')
  break
 elif l3 == ' O  ' and l6 == ' O  ' and l9 == ' O  ':
  print('O won !!!')
  break
 elif l1 == ' O  ' and l5 == ' O  ' and l9 == ' O  ':
  print('O won !!!')
  break
 elif l3 == ' O  ' and l5 == ' O  ' and l7 == ' O  ':
  print('O won !!!')
  break





 if sum % 2 == 0:
  mark = ' X  '
  x = int(input('x: '))
  y = int(input('y: '))
  if x < 4 and x > 0 and y < 4 and y > 0:
   if not [x,y] in list:
    list.append([x,y])
    sum += 1
    if x == 1 and y == 1:
     l1 = mark
    elif x == 1 and y == 2:
     l2 = mark
    elif x == 1 and y == 3:
     l3 = mark
    elif x == 2 and y == 1:
     l4 = mark
    elif x == 2 and y == 2:
     l5 = mark
    elif x == 2 and y == 3:
     l6 = mark
    elif x == 3 and y == 1:
     l7 = mark
    elif x == 3 and y == 2:
     l8 = mark
    elif x == 3 and y == 3:
     l9 = mark



 if sum % 2 != 0:
  mark = ' O  '
  while True:
   x1 = randint(1,3)
   y1 = randint(1,3)
   if not [x1,y1] in list:
    list.append([x1,y1])
    sum += 1
    if x1 == 1 and y1 == 1:
     l1 = mark
    elif x1 == 1 and y1 == 2:
     l2 = mark
    elif x1 == 1 and y1 == 3:
     l3 = mark
    elif x1 == 2 and y1 == 1:
     l4 = mark
    elif x1 == 2 and y1 == 2:
     l5 = mark
    elif x1 == 2 and y1 == 3:
     l6 = mark
    elif x1 == 3 and y1 == 1:
     l7 = mark
    elif x1 == 3 and y1 == 2:
     l8 = mark
    elif x1 == 3 and y1 == 3:
     l9 = mark
    break
 

