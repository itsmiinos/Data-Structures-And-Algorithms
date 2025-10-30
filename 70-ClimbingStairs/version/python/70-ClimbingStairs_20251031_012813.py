# Last updated: 10/31/2025, 1:28:13 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.doDP(n , dp)

    def doDP(self , n , dp) -> int : 
        if n <= 2 : 
            return n

        if dp[n] != -1 : 
            return dp[n]
        
        if n == 0 : 
            return 1
        
        dp[n] = self.doDP(n-1 , dp) + self.doDP(n-2 , dp)
        
        return dp[n]
