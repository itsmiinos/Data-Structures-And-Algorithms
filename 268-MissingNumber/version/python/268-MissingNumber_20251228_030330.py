# Last updated: 12/28/2025, 3:03:30 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        for i in range(len(nums)) :
4            while nums[i] < len(nums) and nums[i] != i:
5                correct = nums[i]
6                nums[i], nums[correct] = nums[correct], nums[i]
7        
8        for i in range(len(nums)) :
9            if nums[i] != i :
10                return i
11            
12        return len(nums)