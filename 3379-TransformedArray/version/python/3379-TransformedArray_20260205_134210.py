# Last updated: 2/5/2026, 1:42:10 PM
1class Solution:
2    def constructTransformedArray(self, nums: List[int]) -> List[int]:
3        result = [0]*len(nums)
4
5        for i in range(len(nums)) :
6            val = nums[i]
7            if val != 0 :
8                result[i] = nums[(i + val) % len(nums)]
9            else :
10                result[i] = nums[i]
11        
12        return result
13            