# Last updated: 6/29/2026, 8:08:19 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left = 0
4        right = 0
5        max_profit = 0
6
7        while right < len(prices) :
8            if prices[right] < prices[left] :
9                left = right
10            
11            else :
12                max_profit = max(max_profit , prices[right] - prices[left])
13            
14            right+=1
15
16        return max_profit