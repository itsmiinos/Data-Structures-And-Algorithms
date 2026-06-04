# Last updated: 6/4/2026, 11:40:55 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        ans = nums[0]
4        for i in range(1 , len(nums)) :
5            ans = ans ^ nums[i]
6        
7        return ans