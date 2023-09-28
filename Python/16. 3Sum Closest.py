'''
1. Sort the nums array in ascending order.

2. Initialize a variable closest to store the closest sum found so far. Set it to a large value initially.

3. Iterate through the nums array with a fixed starting element. For each element at index i, set two pointers left and right initially to the elements at indices i+1 and n-1, respectively.

4. While left is less than right, calculate the sum of the elements at indices i, left, and right, i.e., current = nums[i] + nums[left] + nums[right].

5. If currentSum is equal to the target, return currentSum as it's the closest possible sum.

6. If the absolute difference between currentSum and target is smaller than the absolute difference between closestSum and target, update closestSum to be equal to currentSum.

7. If currentSum is less than target, increment the left pointer to explore larger values.

8. If currentSum is greater than target, decrement the right pointer to explore smaller values.

9. Continue this process until left is less than right. Then, move on to the next element at index i and repeat steps 4-9.

10. Finally, return the closest as the answer.
'''

def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current = nums[i] + nums[left] + nums[right]

            if current == target:
                return current

            if abs(current - target) < abs(closest - target):
                closest = current

            if current < target:
                left += 1
            else:
                right -= 1

    return closest

# Example usage:
nums1 = [-1, 2, 1, -4]
target1 = 1
print(threeSumClosest(nums1, target1))  # Output: 2

nums2 = [0, 0, 0]
target2 = 1
print(threeSumClosest(nums2, target2))  # Output: 0
