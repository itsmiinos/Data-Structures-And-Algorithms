# Last updated: 9/17/2025, 9:44:24 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices)+1)]

        #0 -> True
        #1 -> False

        dp[len(prices)][0] = 0
        dp[len(prices)][1] = 0

        
        for i in range(len(prices)-1 , -1 , -1) : 
            for j in range(2) : 

                if j == 0 : 
                    dp[i][j] = max(-prices[i] + dp[i+1][1] , dp[i+1][0])
                else : 
                    sell = prices[i]
                    if i+2 < len(dp) : 
                        sell += dp[i+2][0]
                    not_sell = dp[i+1][1]  
                    dp[i][j] = max(sell , not_sell)

        
        return dp[0][0]