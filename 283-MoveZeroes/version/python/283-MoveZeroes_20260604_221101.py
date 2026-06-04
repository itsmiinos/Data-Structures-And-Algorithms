# Last updated: 6/4/2026, 10:11:01 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        j = 0
7        for i in range(len(nums)) :
8            if nums[i] != 0 :
9                nums[j] = nums[i]
10                j+=1
11        
12        while j < len(nums) :
13            nums[j] = 0
14            j+=1
15        