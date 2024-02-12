class Car:
    def __init__(self,name:str,speed:int):
        self.name = name
        self.speed = speed
    def info(self):
        return f'Name: {self.name} \nSpeed: {self.speed}'
    def nameOut(self):
        return self.name
    def speedOut(self):
        return self.speed
    def __str__(self):
        return 'Car'


class Bugati(Car):
    def __init__(self, name:str, speed:int, color:list):
        super().__init__(name, speed)
        self.color = color
    def colorOut(self):
        for i in self.color:
            return i
    def all(self):
        return f'Name: {self.name} \nSpeed: {self.speed} \nColor: {self.color}'
    def __str__(self):
        return self.name
    

class Lamborgini(Car):
    def __init__(self, name:str, speed:int, weight:int):
        super().__init__(name, speed)
        self.weight = weight
    def colorOut(self):
            return self.weight
    def all(self):
        return f'Name: {self.name} \nSpeed: {self.speed} \nColor: {self.weight}'
    def __str__(self):
        return self.name
    

one = Bugati('Bugati',100,['red','blue'])
two = Lamborgini('Lamborgini',150,20)

print(one.all())
print('_________\n')
print(two.all())