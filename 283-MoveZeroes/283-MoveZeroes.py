# Last updated: 8/13/2025, 8:20:22 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range (len(nums)) :
            if nums[i]!=0 :
                [nums[i] , nums[j]] = [nums[j] , nums[i]]
                j+=1
