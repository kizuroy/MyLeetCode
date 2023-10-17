def rotate(nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]