class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.knapsackHelper(W, val, wt, n - 1, dp)
        
    def knapsackHelper(self, W, val, wt, i, dp):
        if i < 0 or W == 0:
            return 0
        if dp[i][W] != -1:
            return dp[i][W]

        # Exclude current item
        not_pick = self.knapsackHelper(W, val, wt, i - 1, dp)

        # Include current item if it fits
        pick = -1
        if wt[i] <= W:
            pick = val[i] + self.knapsackHelper(W - wt[i], val, wt, i - 1, dp)

        dp[i][W] = max(pick, not_pick)
        return dp[i][W]
