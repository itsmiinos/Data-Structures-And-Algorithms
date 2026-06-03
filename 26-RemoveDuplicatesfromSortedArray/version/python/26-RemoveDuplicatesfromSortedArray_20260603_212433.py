# Last updated: 6/3/2026, 9:24:33 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        j = 0
4        for i in range(1 , len(nums)) :
5            if nums[i] != nums[j] :
6                j+=1
7                nums[j] = nums[i]
8        
9        return j+1