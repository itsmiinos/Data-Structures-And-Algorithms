# Last updated: 1/5/2026, 9:56:49 PM
1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        total = 0
4        neg_count = 0
5        min_abs = float('inf')
6
7        for row in matrix:
8            for val in row:
9                if val < 0:
10                    neg_count += 1
11                abs_val = abs(val)
12                total += abs_val
13                min_abs = min(min_abs, abs_val)
14
15        if neg_count % 2 == 1:
16            total -= 2 * min_abs
17
18        return total
19