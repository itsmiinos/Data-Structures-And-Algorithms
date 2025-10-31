# Last updated: 10/31/2025, 11:01:02 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        # return max(self.doDP(0 , nums,dp) , self.doDP(1 , nums , dp))

        dp[0] = nums[0]

        for i in range(1 , len(nums)) : 
            take = nums[i]
            if i > 1 : 
                take += dp[i-2]

            not_take = dp[i-1]

            dp[i] = max(take , not_take)
        
        return dp[len(nums)-1]
            

    # def doDP(self , src : int , nums : list[int] , dp : list[int]) -> int : 
    #     if src >= len(nums) :
    #         return 0
        
    #     if dp[src] != -1 : 
    #         return dp[src]
        
    #     take_loot = self.doDP(src+2 , nums , dp) + nums[src]
    #     leave_loot = self.doDP(src+1 , nums , dp)

    #     dp[src] = max(take_loot , leave_loot)

    #     return dp[src]