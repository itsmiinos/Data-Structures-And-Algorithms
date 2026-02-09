# Last updated: 2/9/2026, 1:59:19 PM
1class Solution:
2    def maxScore(self, nums1: List[int], nums2: List[int], K: int) -> int:
3        n, m = len(nums1), len(nums2)
4        NEG_INF = float('-inf')
5
6        dp = [[[NEG_INF] * (K + 1) for _ in range(m + 1)] for _ in range(n + 1)]
7
8        # base case: 0 pairs → 0 score
9        for i in range(n + 1):
10            for j in range(m + 1):
11                dp[i][j][0] = 0
12
13        for i in range(n - 1, -1, -1):
14            for j in range(m - 1, -1, -1):
15                for t in range(1, K + 1):
16                    skip_i = dp[i + 1][j][t]
17                    skip_j = dp[i][j + 1][t]
18                    take = nums1[i] * nums2[j] + dp[i + 1][j + 1][t - 1]
19
20                    dp[i][j][t] = max(skip_i, skip_j, take)
21
22        return dp[0][0][K]