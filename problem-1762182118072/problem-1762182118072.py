# Last updated: 11/3/2025, 8:31:58 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        return self.solve(nums , len(nums)-1 , target , dp)

    
    def solve(self , nums : list , index : int , target : int , dp : tuple) -> int : 

        if index < 0 : 
            if target == 0 : 
                return 1
            else : 
                return 0

        if (index , target) in dp : 
            return dp[(index , target)]

  
        
        take = self.solve(nums , index - 1 , target - nums[index] , dp)
        dont_take = self.solve(nums , index - 1 , target + nums[index] , dp)

        dp[(index , target)] = take + dont_take

        return dp[(index , target)]