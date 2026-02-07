# Last updated: 2/7/2026, 10:10:08 PM
1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        res = 0
4        count = 0
5        for ch in s:
6            if ch == 'b':
7                count += 1
8            elif count:
9                res += 1
10                count -= 1
11        
12        return res