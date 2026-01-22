# Last updated: 1/22/2026, 9:21:08 PM
1from typing import List
2
3class Solution:
4    def minimumPairRemoval(self, nums: List[int]) -> int:
5        count = 0
6
7        while nums != sorted(nums):
8            index = self.minPairSum(nums)
9            pairSum = nums[index] + nums[index + 1]
10            nums[index:index + 2] = [pairSum]
11            count += 1
12
13        return count
14
15    def minPairSum(self, nums: list) -> int:
16        min_sum_index = 0
17        for i in range(len(nums) - 1):
18            if nums[i] + nums[i + 1] < nums[min_sum_index] + nums[min_sum_index + 1]:
19                min_sum_index = i
20        return min_sum_index
21