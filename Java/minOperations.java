import java.util.Arrays;

class Solution {
    public int minOperations(int[] nums, int x) {
        int target = Arrays.stream(nums).sum() - x;
        
        if (target < 0) {
            return -1;
        }
        
        if (target == 0) {
            return nums.length;
        }
        
        int left = 0;
        int currentSum = 0;
        int minOps = Integer.MAX_VALUE;
        
        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];
            
            while (currentSum > target) {
                currentSum -= nums[left];
                left++;
            }
            
            if (currentSum == target) {
                minOps = Math.min(minOps, nums.length - (right - left + 1));
            }
        }
        
        return minOps != Integer.MAX_VALUE ? minOps : -1;
    }
}

