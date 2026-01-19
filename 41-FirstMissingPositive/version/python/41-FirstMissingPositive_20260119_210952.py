# Last updated: 1/19/2026, 9:09:52 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        i = 0 
6        while ( i < n) : 
7            if nums[i] <1 or nums[i] >n-1 or nums[i]-1 == i: 
8                i+=1
9            
10            else : 
11                correctIndex = nums[i]-1
12                if nums[correctIndex] == nums[i] : i+=1
13                else : [nums[i] , nums[correctIndex]] = [nums[correctIndex] , nums[i]]
14        print(nums)
15        for i in range(n) : 
16            if nums[i]-1 != i : 
17                return i+1
18        return n+1