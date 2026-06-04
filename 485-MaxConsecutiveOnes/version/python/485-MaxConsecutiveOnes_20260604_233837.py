# Last updated: 6/4/2026, 11:38:37 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        count = 0
4        max_count = 0
5        for i in range(len(nums)) :
6            if nums[i] == 1 :
7                count+=1
8                max_count = max(count , max_count)
9            else :
10                count = 0
11        
12        return max_count