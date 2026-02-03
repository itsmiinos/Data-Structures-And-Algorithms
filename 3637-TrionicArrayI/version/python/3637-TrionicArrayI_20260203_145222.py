# Last updated: 2/3/2026, 2:52:22 PM
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3
4        i = 0
5        while i+1 < len(nums) and nums[i] < nums[i+1]:
6            i+=1
7        
8        if i == 0 or i == len(nums)-1 :
9            return False
10        
11        while i+1 < len(nums) and nums[i] > nums[i+1]:
12            i+=1
13        
14        if i == len(nums)-1 :
15            return False
16        
17        while i+1 < len(nums) and nums[i] < nums[i+1]:
18            i+=1
19        
20        return i == len(nums)-1
21