class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_steps = len(cost)
        res = 0
        dp = [-1]*total_steps
        result = min (self.climblingStairsHelper(total_steps-1 , cost , res, dp) , self.climblingStairsHelper(total_steps-2 , cost , res , dp))
        return result
    
    def climblingStairsHelper(self , n:int , cost:[int], res:int , dp:[int]) -> int:
        if n==0 or n==1 :
            return cost[n]
        if dp[n] != -1 : return dp[n]
        res = cost[n] + min(self.climblingStairsHelper(n-1 , cost , res , dp),self.climblingStairsHelper(n-2 , cost , res, dp))
        dp[n] = res
        return res