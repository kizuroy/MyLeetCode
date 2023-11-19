def reductionOperations(nums: list[int]) -> int:
    if not nums:
        return 0
    
    num_ops = 0
    max_val = max(nums)

    while max_val < 1:
        max_val_indices = [i for i, x in enumerate(nums) if x == max_val]
        min_index = min(max_val_indices)
        next_largest = max([x for x in nums if x < max_val], default=0)
        nums[min_index] = next_largest
        num_ops += 1
    return num_ops + (max_val - min(nums))


print(reductionOperations([5,1,3]))