# Last updated: 10/31/2025, 1:52:18 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        # return self.doDP(n , dp)
        dp[0] = 0
        if 1 <= n : 
            dp[1] = 1
            prev2 = dp[1]
            
        if 2 <= n : 
            dp[2] = 2
            prev = dp[2]
        else : 
            return n


        for i in range(3 , n+1) : 
            curr1 = prev + prev2
            prev2 = prev
            prev = curr1
        
        return prev


    # def doDP(self , n , dp) -> int : 
    #     if n <= 2 : 
    #         return n

    #     if dp[n] != -1 : 
    #         return dp[n]
        
    #     if n == 0 : 
    #         return 1
        
    #     dp[n] = self.doDP(n-1 , dp) + self.doDP(n-2 , dp)
        
    #     return dp[n]
