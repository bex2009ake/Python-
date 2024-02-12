# import json


# with open('data.json','r') as r:
#     text = r.read()
#     text = json.load(text)
#     text['job'] = 'Student'

# with open('data.json','w') as w:
#     text = json.dump(text,indent=2)
#     w.write(str(text))



nums = []


for i in range(10,1,-1):
 for j in range(0,11):
    if i + j == 10:
     nums.append(i+j)
     print(i,j)

print(nums)



# for i in range(10,0,-1):
#   print([[i,j] for j in range(0,11) if i + j == 10])



print([[i,j] for i in range(10,0,-1) for j in range(0,11) if i + j == 10])
