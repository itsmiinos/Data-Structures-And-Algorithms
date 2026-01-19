# Last updated: 1/19/2026, 9:30:08 PM
1class Solution:
2    def isValid(self, pref, k, limit):
3        n = len(pref)
4        m = len(pref[0])
5
6        for i in range(k - 1, n):
7            for j in range(k - 1, m):
8                x1 = i - k + 1
9                y1 = j - k + 1
10
11                total = pref[i][j]
12                if x1 > 0:
13                    total -= pref[x1 - 1][j]
14                if y1 > 0:
15                    total -= pref[i][y1 - 1]
16                if x1 > 0 and y1 > 0:
17                    total += pref[x1 - 1][y1 - 1]
18
19                if total <= limit:
20                    return True
21
22        return False
23
24    def maxSideLength(self, mat, threshold):
25        n = len(mat)
26        m = len(mat[0])
27
28        pref = [row[:] for row in mat]
29
30        # Row-wise prefix sum
31        for i in range(n):
32            for j in range(1, m):
33                pref[i][j] += pref[i][j - 1]
34
35        # Column-wise prefix sum
36        for j in range(m):
37            for i in range(1, n):
38                pref[i][j] += pref[i - 1][j]
39
40        low, high = 1, min(n, m)
41        ans = 0
42
43        while low <= high:
44            mid = (low + high) // 2
45            if self.isValid(pref, mid, threshold):
46                ans = mid
47                low = mid + 1
48            else:
49                high = mid - 1
50
51        return ans