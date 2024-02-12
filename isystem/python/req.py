import csv


with open('a.csv','w',newline='') as file:
    w = csv.DictWriter(file,delimiter=',')
    w.writerow(['1','a'])
    w.writerow(['2','b'])
    w.writerow(['3','c'])

