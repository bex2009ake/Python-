# all = []


# def carOutput():
#     for i in all:
#        print(i)

# def carInput():

#     while True:
#       inf = {}

#       stop = input('Stop: ').capitalize()

#       if stop == 'Yes':
#         break
#       else:
#         all.append(inf)
#         name = input('Name: ')
#         year = int(input('Year: '))
#         color = input('Color: ')
    
#         inf['nmae'] = name
#         inf['year'] = year 
#         inf['color'] = color
#         print(inf)



all = []


def studentsOutput():
  for student in all:
    print(student,end='\n')


def studentsInput(name,age,number,hobby,id=len(all)):
    int(age)
    int(id)
    info = {}
    info['name'] = name
    info['age'] = age
    info['phone-num'] = number
    info['hobby'] = str(hobby).split()
    all.append(info)


def main():
  while True:
    if len(all) >= 5:
      studentsOutput()
      break
    else:
      studentsInput(name=input('Name: '),
        age=int(input('Age: ')),
        number=input('Phone-num: '),
        hobby=input('Hobbies: '))

