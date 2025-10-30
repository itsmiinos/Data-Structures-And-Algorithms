# Last updated: 10/31/2025, 1:31:20 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        # return self.doDP(n , dp)
        dp[0] = 0
        if 1 <= n : dp[1] = 1
        if 2 <= n : dp[2] = 2

        for i in range(3 , n+1) : 
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


    # def doDP(self , n , dp) -> int : 
    #     if n <= 2 : 
    #         return n

    #     if dp[n] != -1 : 
    #         return dp[n]
        
    #     if n == 0 : 
    #         return 1
        
    #     dp[n] = self.doDP(n-1 , dp) + self.doDP(n-2 , dp)
        
    #     return dp[n]
