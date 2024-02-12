import random


class Car:
    def __init__(self,name:int = None,speed:int = None,color:str = None,price:int = None,num:int = random.randint(1000,9000)):
        self.name = name
        self.speed = speed
        self.color = color   
        self.price = price   
        self.num = num
    def allInfo(self):
        return(f'Name: {self.name}\nSpeed: {self.speed}\nColor: {self.color}\nPrice: {self.price}\nNum: {self.num}')   
    def akisa(self):
        return(f'20% Before: {self.price} After: {(self.price)-((self.price/100)*20)}')
    def add(self):
        return(f'Additional 30% speed Before: {self.speed} After: {int((self.speed)+((self.speed/100)*30))}')
    def change(self,num2):
        self.num = num2
        return self.num
    def __str__(self) :
        return self.name

BMW = Car(name='BMW',speed=150,color='Dark blue',price=1500)
MERS = Car(name='MERS',color='Black',price=2500,num=4327)
LAMBORGINI = Car(name='LAMBORGINI',color='Red')


for i in [BMW,MERS,LAMBORGINI]:
    print(i.allInfo())
    print("=============")

print([BMW,MERS,LAMBORGINI])