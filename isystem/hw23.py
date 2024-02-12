import datetime
import csv


class Shop:
    def __init__(self, price: int, name: str):
        self.price = price
        self.name = name
        self.date = datetime.date.today()
        self.__bonus = self.price - ((self.price / 100)*15)
    def all(self):
        return f'Name: {self.name}\nPrice: {self.price}\nDate: {self.date}'
    def bonus(self,password):
        return self.__bonus if password == '123' else 'NO'
    def __str__(self):
        return 'Shop'


class Clothes(Shop):
    def __init__(self, price: int, name: str, size:int):
        super().__init__(price, name)
        self.size = size
    def all(self):
        return f'Name: {self.name}\nPrice: {self.price}\nDate: {self.date}\nSize: {self.size}'
    def __str__(self):
        return 'Clothes'
    

class Food(Shop):
    def __init__(self, price: int, name: str, cal:int):
        super().__init__(price, name)
        self.cal = cal
    def all(self):
        return f'Name: {self.name}\nPrice: {self.price}\nDate: {self.date}\nCal: {self.cal}'
    def __str__(self):
        return 'Food'
    


while True:
    a = input('Stop: ')
    if a.lower() == 'yes':
        with open('clothe.csv','r',newline='') as clothe1:
            read = csv.DictReader(clothe1,delimiter=',')  
            print('Clothes')
            for i in read:
                print(f'Name: {i["name"]}, Price: {i["price"]}, Size: {i["size"]}, Time: {i["date"]}, Bonus: {i["bonus"]}')
        with open('food.csv','r',newline='') as food1:
            read = csv.DictReader(food1,delimiter=',')
            print('Food')
            for i in read:
                print(f'Name: {i["name"]}, Price: {i["price"]}, Cal: {i["cal"]}, Time: {i["date"]}, Bonus: {i["bonus"]}')
        break
    else:
        group = input('Group: ')
        if group == 'clothes':
         with open('clothe.csv','a',newline='') as clothe:
            write = csv.writer(clothe,delimiter=',')
            c =Clothes(name=input('Name: '),price=int(input('Price: ')),size=int(input('Size: ')))
            write.writerow([c.name,c.price,c.size,c.date,c.bonus(input('Bonus password: '))])

        else:
         with open('food.csv','a',newline='') as food:
            write = csv.writer(food,delimiter=',')
            f = Food(name=input('Name: '),price=int(input('Price: ')),cal=int(input('Cal: ')))          
            write.writerow([f.name,f.price,f.cal,f.date,f.bonus(input('Bonus password: '))])