# Last updated: 1/2/2026, 12:44:51 PM
1from collections import defaultdict
2class Solution:
3    def repeatedNTimes(self, nums: List[int]) -> int:
4        hashmap = defaultdict(int)
5        for i in range(len(nums)) :
6            hashmap[nums[i]] +=1
7            if hashmap[nums[i]] == len(nums)//2 : return nums[i]
8    
9    