# Last updated: 8/13/2025, 8:19:04 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost)+1)
        result = min (self.helper(len(cost)-1 , cost , dp) , self.helper(len(cost)-2 , cost , dp))
        return result
    
    def helper(self , i : int , cost : [int] , dp : [int]) -> int :

        if i == 0 or i ==1 : 
            return cost[i]
        
        if i < 0 : 
            return +sys.maxsize

        if dp[i] !=-1 : return dp[i]
        temp1 = self.helper(i-1 , cost , dp)
        temp2 = self.helper(i-2 , cost , dp)

        ans = min(temp1 , temp2) + cost[i]
        dp[i] = ans
        return ans 