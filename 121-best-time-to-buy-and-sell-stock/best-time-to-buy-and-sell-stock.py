class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = float('-inf')

        while right < len(prices) :
            max_profit = max(prices[right] - prices[left] , max_profit)

            if prices[right] < prices[left] :
                left = right
                right+=1
            else :
                right+=1
        
        return max_profit
            