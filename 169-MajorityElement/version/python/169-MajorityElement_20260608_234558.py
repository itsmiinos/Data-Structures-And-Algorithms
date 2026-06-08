# Last updated: 6/8/2026, 11:45:58 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        value = -1
4        count = 0
5
6        for i in range(len(nums)) :
7            if count == 0 :
8                value = nums[i]
9
10            if nums[i] == value :
11                count+=1
12            else :
13                count-=1
14        
15        return value