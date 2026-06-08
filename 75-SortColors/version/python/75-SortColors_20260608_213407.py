# Last updated: 6/8/2026, 9:34:07 PM
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
12                nums[i] , nums[j] = nums[j] , nums[i]
13                i+=1
14                j+=1
15            
16            elif nums[j] == 2 :
17                nums[j] , nums[k] = nums[k] , nums[j]
18                k-=1
19
20            else :
21                j+=1 