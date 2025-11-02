# Last updated: 11/2/2025, 7:56:57 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [-1]*len(nums)
        dp2 = [-1]*len(nums)

        if len(nums) == 0 : 
            return 0
        
        if len(nums) == 1 : 
            return nums[0]

        ans = max(self.solve(0,len(nums)-2 , nums , dp1) , self.solve(1 , len(nums)-1 , nums , dp2))
        return ans
    
    def solve(self , start : int , end : int , nums : list , dp : list) -> int : 

        if end == start : 
            return nums[start]
        
        if end < start : 
            return 0
        
        if dp[end]!= -1 : 
            return dp[end]
        
        rob = self.solve(start , end - 2 , nums, dp) + nums[end]
        dont_rob = self.solve(start , end-1 , nums , dp)

        dp[end] = max(rob , dont_rob)

        return dp[end]