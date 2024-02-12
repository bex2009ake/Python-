nums = [2,4,1,0,4,7,3,6,36,25,7,37,92,81,1]


for i in range(len(nums)-1):
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]


print(nums)