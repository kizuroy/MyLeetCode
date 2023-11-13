#Using two pointer:
def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    slow = 2
    fast = 2

    while fast < len(nums):

        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

        fast += 1

    return slow
