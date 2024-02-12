class Student:
    def __init__(self,id:int,name:str = None,age:int = None):
        self.name = name
        self.id = id
        self.age = age
    def names(self):
        return self.name
    def ages(self):
        return self.age
    def all(self):
        return f'Num: {self.id}\nName: {self.name}\nAge: {self.age}'
    def __str__(self):
        return 'Students info'

list = []

for i in range(int(input())):
    list.append(Student(id=i+1,name=input('Name: '),age=int(input('Age: '))))

print(f'1) Name\n2) Age\n3) All')
ask = input('What do you want ?:')

match ask:
    case '1':
        for i in list:
            print(i.names())
            print('_________________')
    case '2':
        for i in list:
            print(i.ages())
            print('_________________')
    case '3':
        for i in list:
            print(i.all())
            print('_________________')
    case _:
        print('Error')