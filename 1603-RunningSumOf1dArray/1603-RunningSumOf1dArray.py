# Last updated: 8/13/2025, 8:17:21 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [None]*len(nums)
        result[0] = nums[0]
        for i in range(1,len(nums)) : 
            result[i] = result[i-1] + nums[i]
        return result