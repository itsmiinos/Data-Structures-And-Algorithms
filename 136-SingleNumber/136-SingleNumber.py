# Last updated: 8/13/2025, 8:22:27 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range (len(nums)) : 
            res = res ^ nums[i]

        return res