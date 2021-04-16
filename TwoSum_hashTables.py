#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def twoSum(nums, target):

    flag = True
    while flag: 
        for i in nums:
            for j in nums: 
                if i + j == target:  
                    print([nums.index(i), nums.index(j)])
                flag = False 
    
    pass
                    
                
#twoSum(nums, target)

def twoSum(nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

nums = [2,7,11,15]
target = 9
    
print(twoSum(nums, target))
