class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        ans = 0
        for n in nums:
            remainder = n % k
            for i in range(k):
                dp[remainder][i] = dp[i][remainder] + 1
                ans = max(ans, dp[remainder][i])
        return ans