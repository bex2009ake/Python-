class Decide:
    def __init__(self,nums):
        self.nums = nums
    
    # def push(self,el):
    #    n = str(self.nums).split(',')
    #    n.append(el)
    # def pop(self,el=-1):
    #     n = str(self.nums).split(',')
    #     n.pop(el)
    # def delet(self,el):
    #    n = str(self.nums).split(',')
    #    n.remove(el)

    def decide(self):
      num = []
      mark = []

      for i in str(self.nums).split(','):
        if str(i).isdigit():
           num.append(i)
        else:
           mark.append(i)
      print(eval(f'{num[-1]}{mark[0]}{num[-2]}'))
    #   print(f'{num.remove(num[-1])}{mark.pop(0)}{num.remove(num[-2])}')
      while True:
         if len(num) == 1 or len(mark) == 0:
            return num

         num.append(eval(f'{num[-1]}{mark[0]}{num[-2]}'))
         print(eval(f'{num[-1]}{mark[0]}{num[-2]}'))
         num.remove(num[-1])
         mark.pop(0)
         num.remove(num[-2])
         print(num)
    

a = Decide('1,2,3,+,-')

print(a.decide())