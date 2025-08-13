# Last updated: 8/13/2025, 8:16:25 PM
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        for i in range(len(nums)) : 
            maxOR = maxOR | nums[i]
        result = self.helper(0 , 0 , nums , maxOR)
        return result

    def helper(self , i , currOR , nums , maxOR) : 

        if i > len(nums)-1 : 
            if currOR == maxOR :
                return 1
            else : 
                return 0

        
        a = self.helper(i+1 , currOR | nums[i] , nums , maxOR)
        
        b = self.helper(i+1 , currOR , nums , maxOR)

        return a + b