def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num # We use the XOR operator.

    return result

print(singleNumber([2,2,1]))        # Output: 1
print(singleNumber([4,1,2,1,2]))    # Output: 4
print(singleNumber([1]))            # Output: 1
