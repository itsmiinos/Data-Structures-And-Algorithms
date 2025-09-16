# Last updated: 9/16/2025, 10:59:10 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        buy = True
        result = self.doDP(prices , 0 , buy ,dp)

        return result

    
    def doDP(self , prices : list[int] , index : int , buy : bool , dp : list) -> int : 

        if index == len(prices) : 
            return 0
        
        if dp[index][buy] != -1 : 
            return dp[index][buy]
        
        profit = 0

        if buy : 
            profit = max(-prices[index] + self.doDP(prices , index+1 , False , dp) , self.doDP(prices , index+1 , True , dp))
        
        else : 
            profit = max(prices[index] + self.doDP(prices , index+1 , True , dp) , self.doDP(prices , index+1 , False , dp))
        
        dp[index][buy] = profit

        return profit