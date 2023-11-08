#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def twoSum(nums, target):
    idxs = dict()
    for idx, num in enumerate(nums):
        if (target - num) in idxs:
            return [idxs[target-num], idx]
        idxs[num] = idx
    return []

print(twoSum([2,7,11,15], 9))