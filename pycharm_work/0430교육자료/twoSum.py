# https://leetcode.com/problems/two-sum/
nums = [2, 7, 9, 11]

def twoSum(nums, target):
    for i in range(len(nums)-1): # O(N)
        for j in range(i+1, len(nums)): #O(N)
            if nums[i] + nums[j] == target:
                return [i, j]
# 시간복잡도 -> O(N^2)

# 개선
def twoSum(nums, target):
    for i, num in enumerate(nums): # O(N)
        res = target - num 
        if res in nums[i+1::]: # O(N) 
            return [i, i+nums[i+1::].index(res)+1] #O(1)
#시간복잡도 -> O(N^2)

# 개선 
def twoSum(nums, target):
    dicts = {}
    for i, num in enumerate(nums): # O(N)
        res = target - num 

        if res in dicts: # dicts의 검색 시간 복잡도: O(1)
            return [i, dicts[res]]

        dicts[num] = i # 숫자와 인덱스를 딕셔너리에 저장 

# 시간복잡도 -> O(N)


















