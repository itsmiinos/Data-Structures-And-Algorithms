# Last updated: 9/17/2025, 9:46:38 PM
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices)+1)]

        #0 -> True
        #1 -> False

        dp[len(prices)][0] = 0
        dp[len(prices)][1] = 0

        
        for i in range(len(prices)-1 , -1 , -1) : 
            for j in range(2) : 

                if j == 0 : 
                    dp[i][j] = max(-prices[i] - fee + dp[i+1][1] , dp[i+1][0])
                else : 
                    dp[i][j] = max(prices[i] + dp[i+1][0] , dp[i+1][1])

        
        return dp[0][0]