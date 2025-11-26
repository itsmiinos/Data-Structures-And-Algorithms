# Last updated: 11/26/2025, 8:04:20 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left = 0
4        right = 1
5        max_profit = 0
6
7        while right < len(prices) : 
8            max_profit = max(max_profit  , prices[right] - prices[left])
9            if prices[right] < prices[left] : 
10                left = right
11            else : 
12                right +=1
13        
14        return max_profit