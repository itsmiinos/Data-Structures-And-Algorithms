# Last updated: 2/1/2026, 1:20:43 PM
1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        if len(nums) == 3 :
4            return sum(nums)
5        
6        score = nums[0]
7        firstMin = float('inf')
8        secondMin = float('inf')
9
10        for i in range(1 , len(nums)) :
11            if nums[i] <= firstMin :
12                secondMin = firstMin
13                firstMin = nums[i]
14            elif nums[i] <= secondMin :
15                secondMin = nums[i]
16                
17        return score + firstMin + secondMin