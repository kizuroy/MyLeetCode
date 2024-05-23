def canJump(nums) -> bool:
        farthest_reach = 0

        for i, jump in enumerate(nums):
            if i > farthest_reach:
                return False

            farthest_reach = max(farthest_reach, i + jump)

            # Optimization: Check success condition during the loop
            if farthest_reach >= len(nums) - 1:
                return True  

        return False 


print(canJump([2,3,1,1,4])) #True

print(canJump([3,2,1,0,4])) #False