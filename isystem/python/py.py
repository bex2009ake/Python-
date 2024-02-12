# a = input()
# b = ''

# print(a[2])
# print(a[-2])
# print(a[0:5])
# print(a[0:-2])
# for i in range(len(a)):
#     if i % 2 == 0:
#         b += a[i]
# print(b)
# b =''
# for i in range(len(a)):
#     if i % 2 != 0:
#         b += a[i]
# print(b)
# print(a[::-1])
# b =''
# c = a[::-1]
# for i in range(len(c)):
#     if a == 'qwertyuiop':
#      if i % 2 != 0:
#         b += a[i]
#     elif i % 2 == 0:
#         b += a[i]
# print(b[::-1])
# print(len(a))



# import eel

# eel.init('web')

# @eel.expose
# def processData():
#     return {'data':'hello'}


# eel.start('index.html', size=(1000, 2500))

import qrcode
img = 'C:\Users\user\Desktop\python\web\p.jpg'
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")