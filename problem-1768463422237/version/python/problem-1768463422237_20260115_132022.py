# Last updated: 1/15/2026, 1:20:22 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        j = 0
4        for i in range(len(nums)) :
5            if nums[i]!= val :
6                nums[j] = nums[i]
7                j+=1
8        
9        return j