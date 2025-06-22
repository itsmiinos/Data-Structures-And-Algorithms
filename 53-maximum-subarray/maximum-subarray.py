import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        sum = 0
        for i in range(len(nums)) : 
            if sum < 0 : 
                sum = nums[i]
            else : 
                sum = sum + nums[i]

            max_sum = max(sum , max_sum)
        return max_sum