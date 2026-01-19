# Last updated: 1/19/2026, 9:28:53 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        self.dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
4        return self.solve(0 , len(prices) , prices , 0)
5
6    def solve(self , i : int , n : int , prices : list , haveStock : int) -> int :
7        if i >= n : 
8            return 0
9        
10        if self.dp[i][haveStock] != -1 : 
11            return self.dp[i][haveStock]
12        
13        profit = 0
14        if haveStock == 0 : 
15            profit += max(self.solve(i+1 , n , prices , 1) - prices[i] , self.solve(i+1 , n , prices , haveStock))
16        
17        else : 
18            profit += max(self.solve(i+1 , n , prices , haveStock) , self.solve(i+1 , n , prices , 0) + prices[i])
19
20        self.dp[i][haveStock] = profit
21        return profit 