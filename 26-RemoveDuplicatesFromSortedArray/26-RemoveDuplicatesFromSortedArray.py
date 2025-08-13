# Last updated: 8/13/2025, 8:24:11 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        for i in range (len(nums)) :
            if nums[i] != nums[current] :
                current+=1
                nums[current] = nums[i]
        
        return current+1
        