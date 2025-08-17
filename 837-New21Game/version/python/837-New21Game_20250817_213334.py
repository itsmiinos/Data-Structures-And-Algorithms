# Last updated: 8/17/2025, 9:33:34 PM
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window_sum = 1.0 
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return result