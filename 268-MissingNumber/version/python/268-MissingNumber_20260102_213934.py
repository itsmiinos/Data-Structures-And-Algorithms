# Last updated: 1/2/2026, 9:39:34 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        for i in range(len(nums)) :
4            while nums[i] < len(nums) and nums[i] != i :
5                value = nums[i]
6                if nums[i] != nums[value] :
7                    nums[i] , nums[value] = nums[value] , nums[i]
8        
9        for i in range(len(nums)) :
10            if nums[i] != i :
11                return i
12        
13        return len(nums)