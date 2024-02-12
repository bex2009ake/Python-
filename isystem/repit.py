def removeElement(nums,val):
    a = set()
    for i in nums:
        a.add(i)
    a.discard(val)
    return list(a)
print(removeElement([0,1,2,2,3,0,4,2],2))

