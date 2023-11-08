def moveZeroes(nums):
    location = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[location], nums[i] = nums[i], nums[location]
            location += 1