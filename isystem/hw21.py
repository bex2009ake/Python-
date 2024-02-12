class Programming:
    def __init__(self,name,age,iq):
        self.name = name
        self.age = age
        self.iq = iq
    def info(self):
        return f'Name: {self.name}\nAge: {self.age}\nIQ: {self.iq}'
    def nameOut(self):
        return self.name
    def iqOut(self):
        return self.iq
    def ageOut(self):
        return self.ageOut
    def __str__(self):
        return 'ISYSTEM'
    

class Frontend(Programming):
    def __init__(self, name, age, iq, style):
        super().__init__(name, age, iq)
        self.style = style
    def info(self):
        return f'Name: {self.name}\nAge: {self.age}\nIQ: {self.iq}\nStyle: {self.style}'
    def styleOut(self):
        return self.style
    def __str__(self):
        return 'Frontend'


class Backend(Programming):
    def __init__(self, name, age, iq, db):
        super().__init__(name, age, iq)
        self.db = db
    def info(self):
        return f'Name: {self.name}\nAge: {self.age}\nIQ: {self.iq}\nStyle: {self.db}'
    def dbOut(self):
        return self.db
    def __str__(self):
        return 'Backend'

front = []    


for i in range(int(input('Frontend: '))):
   name = input('Name: ')
   age = int(input('Age: '))
   iq = int(input('IQ: '))
   styletool = input('Style tool: ')

   front.append(Frontend(name=name, age=age, iq=iq, style=styletool))


back = []    


for i in range(int(input('Backend: '))):
   name = input('Name: ')
   age = int(input('Age: '))
   iq = int(input('IQ: '))
   db = input('DB: ')

   back.append(Backend(name=name, age=age, iq=iq, db=db))

print(
"""
1) All
2) Frontend
3) Backend
"""
)

a = int(input(':'))
b = {1:front+back,2:front,3:back}

for i in b[a]:
    print(i.info())
