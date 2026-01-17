# Last updated: 1/17/2026, 9:30:07 PM
1class Solution:
2    def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
3        s = 0
4        n = len(bl)
5
6        for i in range(n):
7            for j in range(i + 1, n):
8                min_x = max(bl[i][0], bl[j][0])
9                max_x = min(tr[i][0], tr[j][0])
10                min_y = max(bl[i][1], bl[j][1])
11                max_y = min(tr[i][1], tr[j][1])
12
13                if min_x < max_x and min_y < max_y:
14                    length = min(max_x - min_x, max_y - min_y)
15                    s = max(s, length)
16
17        return s * s
18