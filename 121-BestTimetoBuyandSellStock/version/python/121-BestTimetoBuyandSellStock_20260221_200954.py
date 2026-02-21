# Last updated: 2/21/2026, 8:09:54 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left = 0
4        right = 0
5        max_profit = 0
6
7        while right < len(prices) :
8            max_profit = max(max_profit , prices[right] - prices[left])
9
10            if prices[right] < prices[left] :
11                left = right
12            
13            right+=1
14        
15        return max_profit
16            
17