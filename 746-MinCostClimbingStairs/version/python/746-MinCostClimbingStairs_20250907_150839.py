# Last updated: 9/7/2025, 3:08:39 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [-1]*len(cost)
        result = min(self.climbStairs(cost , len(cost)-1 , dp) , self.climbStairs(cost , len(cost)-2 , dp))
        return result
    
    def climbStairs(self , cost : int , step : int , dp : list[int]) -> int : 
        if step < 0 : 
            return 0

        if dp[step] != -1 : 
            return dp[step]
        
        min_cost = min(self.climbStairs(cost , step - 1 , dp) , self.climbStairs(cost , step - 2 , dp)) + cost[step]
        dp[step] = min_cost

        return min_cost 

