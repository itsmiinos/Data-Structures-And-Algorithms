# Last updated: 2/17/2026, 8:53:51 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        max_count = 0
4        lookup = set(nums)
5        for num in lookup :
6
7            if (num - 1) not in lookup:
8                curr = num
9                count = 1
10
11                while (curr + 1) in lookup:
12                    curr += 1
13                    count += 1
14
15                max_count = max(max_count, count)
16
17        
18        return max_count