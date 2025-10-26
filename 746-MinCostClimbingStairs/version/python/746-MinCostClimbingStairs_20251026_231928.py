# Last updated: 10/26/2025, 11:19:28 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost)+1)
        return min(self.doDP(len(cost)-1 , dp , cost) , self.doDP(len(cost)-2 , dp , cost))

    def doDP(self , n , dp , cost) -> int : 
        if n < 0 : 
            return 0

        if dp[n] != -1 : 
            return dp[n]
        
        a = self.doDP(n-1 , dp , cost)
        b = self.doDP(n-2 , dp , cost)

        dp[n] = min(a , b) + cost[n]
        
        return dp[n]