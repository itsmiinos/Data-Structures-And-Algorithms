# Last updated: 6/3/2026, 9:19:27 PM
1class Solution:
2    def check(self, nums: List[int]) -> bool:
3        count = 0
4        for i in range(1 , len(nums)) :
5            if nums[i-1] > nums[i] :
6                count+=1
7
8        if nums[-1] > nums[0] :
9            count+=1
10
11        return count <= 1 