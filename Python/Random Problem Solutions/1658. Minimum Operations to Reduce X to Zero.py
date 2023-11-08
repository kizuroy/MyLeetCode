def minOperations(nums, x):
    # Calculate the target sum by subtracting x from the total sum of nums
    target = sum(nums) - x
    
    # If the target is negative, it's impossible to reach, return -1
    if target < 0:
        return -1
    
    # If the target is 0, we can remove all elements to reach 0
    if target == 0:
        return len(nums)
    
    left, right = 0, 0  # Initialize two pointers for the sliding window
    current_sum = 0     # Initialize the current sum within the window
    min_ops = float('inf')  # Initialize a variable to store the minimum operations
    
    while right < len(nums):
        # Expand the window by adding the right element to the current sum
        current_sum += nums[right]
        
        # If the current sum exceeds the target, shrink the window from the left
        while current_sum > target:
            current_sum -= nums[left]
            left += 1
        
        # If the current sum matches the target, update the minimum operations
        if current_sum == target:
            min_ops = min(min_ops, len(nums) - (right - left + 1))
        
        # Move the right pointer to the right to expand the window
        right += 1
    
    # If min_ops is still the initial value, no subarray was found, return -1
    return min_ops if min_ops != float('inf') else -1


nums1 = [1, 1, 4, 2, 3]
x1 = 5
print(minOperations(nums1, x1))  # 2

nums2 = [5, 6, 7, 8, 9]
x2 = 4
print(minOperations(nums2, x2))  # -1

nums3 = [3, 2, 20, 1, 1, 3]
x3 = 10
print(minOperations(nums3, x3))  # 5