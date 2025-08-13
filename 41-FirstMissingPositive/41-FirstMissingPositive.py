# Last updated: 8/13/2025, 8:23:51 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0 
        while ( i < n) : 
            if nums[i] <1 or nums[i] >n-1 or nums[i]-1 == i: 
                i+=1
            
            else : 
                correctIndex = nums[i]-1
                if nums[correctIndex] == nums[i] : i+=1
                else : [nums[i] , nums[correctIndex]] = [nums[correctIndex] , nums[i]]
        print(nums)
        for i in range(n) : 
            if nums[i]-1 != i : 
                return i+1
        return n+1
