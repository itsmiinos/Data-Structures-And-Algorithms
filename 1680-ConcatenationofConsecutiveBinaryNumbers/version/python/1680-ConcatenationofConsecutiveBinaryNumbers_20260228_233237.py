# Last updated: 2/28/2026, 11:32:37 PM
1class Solution:
2    def concatenatedBinary(self, n: int) -> int:
3        MOD = 10**9 + 7
4        res = 0
5        bits = 0
6
7        for i in range(1, n+1):
8            if (i & (i-1)) == 0:
9                bits += 1
10            res = ((res << bits) | i) % MOD
11
12        return res