import qrcode
img = qrcode.make('https://pypi.org/project/qrcode/')
type(img)  

try:
    img.save("file.png")
    print('All right !')
except:
    print('Error')