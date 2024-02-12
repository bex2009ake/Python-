import requests

def times(city):
  url = requests.get(f'https://islomapi.uz/api/present/day?region={city}')
  
  if "{'success': False, 'message': 'Not found'}" == str(url.json()):
      print('False city')
  else:
   name = ["tong_saharlik","quyosh","peshin","asr","shom_iftor","hufton"]
   for i in name:
    print(f'{i.capitalize()}: {url.json()["times"][i]}')

n = 14

count = 0
if n == 0:
    print(0)
for i in range(1,n+1):
    if '1' in str(i):
        count += 1
print(count)