# Last updated: 9/17/2025, 9:33:22 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices)+1)]

        #for buy -> 0-> True and 1 -> False

        result = self.doDP(prices , 0 , 0 , dp , 2)
        return result


    def doDP(self , prices : list[int] , index : int , buy : int , dp : list[list[list[int]]] , cap : int) -> int : 

        if cap == 0 : 
            return 0
        
        if index == len(prices) : 
            return 0
        
        if dp[index][buy][cap] != -1 : 
            return dp[index][buy][cap]
        
        profit = 0
        if buy == 0 :
            profit = max((-prices[index] + self.doDP(prices , index + 1 , 1 , dp , cap )) , self.doDP(prices , index + 1 , 0 , dp , cap))
        
        else : 
            profit = max((prices[index] + self.doDP(prices , index + 1 , 0 , dp , cap - 1)) , self.doDP(prices , index+1 , 1 , dp , cap))

        dp[index][buy][cap] = profit

        return dp[index][buy][cap]