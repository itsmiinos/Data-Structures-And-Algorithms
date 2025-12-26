# Last updated: 12/26/2025, 9:28:44 PM
1class Solution:
2    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
3        arr.sort()
4        n = len(arr)
5        dp = [[arr[i]] for i in range(n)]
6
7        max_len = 1
8        max_seq = dp[0]
9
10        for i in range(n):
11            for j in range(i):
12                if arr[i] % arr[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
13                    dp[i] = dp[j] + [arr[i]]
14
15            if len(dp[i]) > max_len:
16                max_len = len(dp[i])
17                max_seq = dp[i]
18
19        return max_seq