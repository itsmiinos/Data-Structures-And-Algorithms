# Last updated: 8/13/2025, 8:22:33 PM
class Solution(object):
    def maxProfit(self, prices):
        pricesLength = len(prices)
        maxPrefixPrices = [0] * pricesLength
        maxSuffixPrices = [0] * pricesLength
        profit = 0
        maxProfit = -sys.maxint
        
        maxSuffixPrices[pricesLength-1] = prices[pricesLength-1]

        for i in range(len(prices)-2 , -1 , -1) :
            maxSuffixPrices[i] = max(maxSuffixPrices[i+1] , prices[i])
        
        print(maxSuffixPrices)

        maxPrefixPrices[0] = prices[0]

        for i in range(1,len(prices)) :
            maxPrefixPrices[i] = max(maxPrefixPrices[i-1] , prices[i])

        print(maxPrefixPrices)
        
        for i in range(pricesLength-1) :
            profit = maxSuffixPrices[i] - prices[i]
            maxProfit = max(profit , maxProfit)
        
        if maxProfit < 0 :
            return 0
        
        return maxProfit
        