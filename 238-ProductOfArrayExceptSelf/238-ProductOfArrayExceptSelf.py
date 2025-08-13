# Last updated: 8/13/2025, 8:20:42 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        runningProduct = [None]*n
        backwardsProduct = [None]*n

        runningProduct[0] = nums[0]
        for i in range(1 , n) : 
            runningProduct[i] = runningProduct[i-1] * nums[i]
        
        backwardsProduct[n-1] = nums[n-1]
        for i in range(n-2 , -1 , -1) : 
            backwardsProduct[i] = backwardsProduct[i+1] * nums[i]
        
        multiplier = 1
        for i in range(n-1 , 0 , -1) : 
            temp = backwardsProduct[i]
            backwardsProduct[i] = multiplier * runningProduct[i-1]
            multiplier = temp
        
        backwardsProduct[0] = multiplier
        return backwardsProduct