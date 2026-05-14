# Last updated: 5/14/2026, 10:26:27 PM
1class Solution:
2    def isGood(self, nums: List[int]) -> bool:
3        nums.sort()
4
5        max_element = nums[-1]
6
7        if len(nums) < max_element + 1 : 
8            return False
9        
10        if nums[-1] != nums[-2] :
11            return False
12        
13        for i in range(1 , len(nums)) :
14            if nums[i] == nums[i-1] and i != len(nums)-1 : 
15                return False
16        
17        return True
18        
19
20        
21        