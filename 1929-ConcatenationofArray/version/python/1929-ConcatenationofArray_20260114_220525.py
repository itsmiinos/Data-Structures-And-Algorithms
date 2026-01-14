# Last updated: 1/14/2026, 10:05:25 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        for i in range(len(nums)) :
4            nums.append(nums[i])
5        
6        return nums