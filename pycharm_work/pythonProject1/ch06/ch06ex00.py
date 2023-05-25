nums = [2,7,9,11]
target = 9

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j]== target:
            print([i, j])

def twoSum(nums, target):
    dicts = {}
    for i in range(len(nums)):
        dicts[nums[i]]=i
    #print(dicts)

    for i in range(len(nums)):
        res= target - nums[i]
        if res in dicts:

            print([i, dicts[res]])
        dicts[nums[i]]=i
print(twoSum(nums, target))