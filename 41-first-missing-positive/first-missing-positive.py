class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n : 
            if nums[i] <1 or nums[i] > n or nums[i]-1 == i :
                i +=1

            else : 
                index = nums[i]-1
                if nums[index] == nums[i] : i+=1
                else : [nums[index] , nums[i]] = [nums[i] , nums[index]]
        
        for i in range (len(nums)) : 
            if i!=nums[i]-1 : 
                return i+1
        
        return n+1