# Last updated: 1/16/2026, 2:10:38 AM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        i = 0
7        j = 0
8        k = len(nums)-1
9
10        while j <= k :
11            if nums[j] == 0 :
12                nums[j] , nums[i] = nums[i] , nums[j]
13                i+=1
14                j+=1
15            elif nums[j] == 1 : 
16                j+=1
17            elif nums[j] == 2 : 
18                nums[j] , nums[k] = nums[k] , nums[j]
19                k-=1
20    
21        