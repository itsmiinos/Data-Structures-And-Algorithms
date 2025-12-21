class Solution:
    def minCost(self, heights):
        # code here
        n = len(heights)
        dp = [-1] * n
        dp[0] = 0

        for i in range(1 , n) :
            one_step = dp[i-1] + abs(heights[i] - heights[i-1])
            two_step = float('inf')
            if i > 1 :
                two_step = dp[i-2] + abs(heights[i] - heights[i-2])
            
            dp[i] = min(one_step , two_step)
        
        return dp[n-1]