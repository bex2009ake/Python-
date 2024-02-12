# with open('file2.txt','w+') as file:
#     # for i in file:
#     #     print(i)
#     # for i in range(10):
#     #  file.write(f'{i+1}\n')
#     a = file.read()
#     print(a)




# with open('file.txt','r') as file:
#     info = file.read()
# with open('file.txt','w') as file2:   
#     file2.write(info.replace('-',' '))

a = []
with open('file.txt','r') as file:
    info = file.readlines()
    for i in info:
        for j in i:
            txt = ''
            if j == '-':
                j = ' ' 
            txt += str(j)
            a.append(txt)

    print(a)
# with open('file.txt','w') as file2:   
#     a = list(map(list,info))
#     file2.write(str(a))