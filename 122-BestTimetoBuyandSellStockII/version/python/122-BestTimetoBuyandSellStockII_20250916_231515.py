# Last updated: 9/16/2025, 11:15:15 PM
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
                    dp[i][j] = max(prices[i] + dp[i+1][0] , dp[i+1][1])

        
        return dp[0][0]





























    # def maxProfit(self, prices: List[int]) -> int:

    #     dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
    #     buy = True
    #     result = self.doDP(prices , 0 , buy ,dp)

    #     return result

    
    # def doDP(self , prices : list[int] , index : int , buy : bool , dp : list) -> int : 

    #     if index == len(prices) : 
    #         return 0
        
    #     if dp[index][buy] != -1 : 
    #         return dp[index][buy]
        
    #     profit = 0

    #     if buy : 
    #         profit = max(-prices[index] + self.doDP(prices , index+1 , False , dp) , self.doDP(prices , index+1 , True , dp))
        
    #     else : 
    #         profit = max(prices[index] + self.doDP(prices , index+1 , True , dp) , self.doDP(prices , index+1 , False , dp))
        
    #     dp[index][buy] = profit

    #     return profit