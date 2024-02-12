import requests

url = 'http://127.0.0.1:8000/'

req = requests.get(url)

# try:
#     # Открываем файл изображения в бинарном режиме
#     with open('./1.png', 'rb') as image_file:
#         # Передаем данные в виде словаря, включая изображение
#         data = {
#             "title": "Python",
#             "desc": "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms and has a large standard library. It's widely used for web development, data analysis, artificial intelligence, and more.",
#             "author": "Behruz"
#         }

#         files = {'img': ('1.png', image_file, 'image/png')}

#         post = requests.post(url=url, data=data, files=files)

#         print('All right !!!')
# except Exception as e:
#     print(f"Error: {e}")


for i in req.json():
    print(i['img'])