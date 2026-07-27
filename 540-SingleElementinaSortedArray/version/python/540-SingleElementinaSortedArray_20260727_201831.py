# Last updated: 7/27/2026, 8:18:31 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        ans = 0
4        for i in range(len(nums)) :
5            ans = ans ^ nums[i]
6        
7        return ans