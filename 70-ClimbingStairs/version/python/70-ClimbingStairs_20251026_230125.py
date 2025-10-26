# Last updated: 10/26/2025, 11:01:25 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.doDP(n , dp)

    def doDP(self , n , dp) -> int : 
        if n < 0 : 
            return 0

        if dp[n] != -1 : 
            return dp[n]
        
        if n == 0 : 
            return 1
        
        dp[n] = self.doDP(n-1 , dp) + self.doDP(n-2 , dp)
        
        return dp[n]
