import sys,time,datetime,os,math


list = {
    'sys':dir(sys),
    'time':dir(time),
    'datetime':dir(datetime),
    'os':dir(os),
    'math':dir(math)
}


for key,value in list.items():
    print(key,':')
    for i in value:
     print(i,end=', ')
    print('\n======================')