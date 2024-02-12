import csv

class Person:
    __count = 1
    def __init__(self,name,password):
        self.name = name
        self.id = Person.__count
        Person.__count += 1
        self.password = password
    def __str__(self) -> str:
        return 'Hotel'

while True:
 stop = input('Stop: ')
 if stop.lower() == 'yes':
    break
 else:
  with open('hotel.csv','a',newline='') as hotelAdd:
    w = csv.writer(hotelAdd,delimiter=',')
    p = Person(name=input('Name: '),password=input('Password: '))
    w.writerow([p.id,p.name,p.password])

admin = input('Are you admin?: ').lower()

if admin == 'yes':
    password = input('Admin password: ')
    if password == '123':
        with open('hotel.csv','r',newline='') as adm:
            r = csv.DictReader(adm,delimiter=',')
            for i in r:
                print(f'Id: {i["id"]}, Name: {i["name"]}, Password: {i["password"]}')
    else:
        print(False)
else:
    idKey = input('Your id: ')
    with open('hotel.csv','r',newline='') as adm:
        r = csv.DictReader(adm,delimiter=',')
        for i in r:
            if i['id'] == idKey:
                pw = input('Password: ')
                if pw == i['password']:
                    print(f'Id: {i["id"]}, Name: {i["name"]}, Password: {i["password"]}')
                else:
                    print(False)
    