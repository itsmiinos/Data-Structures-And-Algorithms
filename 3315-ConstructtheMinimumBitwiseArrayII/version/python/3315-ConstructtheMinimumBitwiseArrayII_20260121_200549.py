# Last updated: 1/21/2026, 8:05:49 PM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        result = []
4
5        for val in nums:
6            # even numbers are impossible
7            if val % 2 == 0:
8                result.append(-1)
9                continue
10
11            j = 0
12            # count trailing ones
13            while ((val >> j) & 1) == 1:
14                j += 1
15
16            # flip the highest bit of trailing ones
17            x = val ^ (1 << (j - 1))
18            result.append(x)
19
20        return result