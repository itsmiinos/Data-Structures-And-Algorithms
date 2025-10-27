# Last updated: 10/27/2025, 8:06:20 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums))
        return max(self.doDP(0 , nums,dp) , self.doDP(1 , nums , dp))

    def doDP(self , src : int , nums : list[int] , dp : list[int]) -> int : 
        if src >= len(nums) :
            return 0
        
        if dp[src] != -1 : 
            return dp[src]
        
        take_loot = self.doDP(src+2 , nums , dp) + nums[src]
        leave_loot = self.doDP(src+1 , nums , dp)

        dp[src] = max(take_loot , leave_loot)

        return dp[src]