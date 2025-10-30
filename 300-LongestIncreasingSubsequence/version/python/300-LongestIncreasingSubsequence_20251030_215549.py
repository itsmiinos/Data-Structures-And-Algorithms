# Last updated: 10/30/2025, 9:55:49 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        result = self.doDP(nums , 0 , -1 , dp)
        return result

    
    def doDP(self , nums : list[int] , index : int , prev : int , dp : list[int]) -> int : 

        if index == len(nums) : 
            return 0
        
        if dp[index][prev] != -1 : 
            return dp[index][prev]
        
        prev_value = 0
        
        if prev == -1 : 
            prev_value = float('-inf')
        else : 
            prev_value = nums[prev]

        length = 0

        if nums[index] > prev_value : 
            take = 1 + self.doDP(nums , index + 1 , index , dp)
            dont_take = self.doDP(nums , index + 1 , prev , dp)

            length = max ( take , dont_take)
        
        else : 

            length = self.doDP(nums , index + 1 , prev , dp)
        
        dp[index][prev] = length
        return length