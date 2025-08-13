# Last updated: 8/13/2025, 8:20:24 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum =  len(nums)
        for i in range (len(nums)) : 
            sum += (i - nums[i])
        return sum