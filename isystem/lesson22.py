# class Car:
#     __num = 0
#     def __init__(self,name,speed,S):
#         self.name = name
#         self.speed = speed
#         self.__S = S
#         Car.__num += 1
#     def plus_S(self,km):
#         return self.__S + km if km > 0 else f'S = {self.__S}, but you can\'t change it'
#     @classmethod
#     def numOUT(cls):
#         return cls.__num
#     def info(self):
#         return self.name,self.speed
#     def __str__(self):
#         return self.name,self.speed


# list = []



# for i in range(int(input())):
#     if Car.numOUT() == 6:
#         print('Stop')
#         for i in list:
#             print(i.info())
#         break
#     else:
#         list.append(Car(name=input('Name: '),speed=int(input('Speed: ')),S=int(input('S: '))))

def maxSum(nums):
        a = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > 10 and str(nums[i])[::-1] == str(nums[j]):
                    a.add(nums[i]+nums[j])
        if len(a) > 0:
         return max(a)
        else:
            return -1

print(maxSum([1,2,3,4]))