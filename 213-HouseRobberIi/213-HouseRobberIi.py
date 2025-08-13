# Last updated: 8/13/2025, 8:21:12 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [-1]*len(nums)
        dp2 = [-1]*len(nums)
        return max(
            self.robHelper(nums, 0, len(nums) - 2 , dp1),  # Exclude last house
            self.robHelper(nums, 1, len(nums) - 1 , dp2)   # Exclude first house
        )
    
    def robHelper(self , nums , start , end , dp) -> int : 
        if start > end:
            return 0
        if start == end:
            return nums[start]
        if dp[end] !=  -1 : return dp[end]
        # Recursive relation
        dp[end] = max(
            self.robHelper(nums, start, end - 1 , dp),            
            self.robHelper(nums, start, end - 2 , dp) + nums[end] 
        )
        return max(
            self.robHelper(nums, start, end - 1 , dp),            
            self.robHelper(nums, start, end - 2 , dp) + nums[end] 
        )
