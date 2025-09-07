# Last updated: 9/7/2025, 3:15:27 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        result = max(self.helper(len(nums)-1 , nums , dp) , self.helper(len(nums)-2 , nums , dp) )
        return result

    def helper(self , i:int , nums : [int] , dp : [int]) -> int : 
        if i < 0 : 
            return 0
        if i ==0:
            return nums[i]
        if dp[i] !=-1 : return dp[i]
        temp1 = self.helper(i-2 , nums , dp) + nums[i]
        temp2 = self.helper(i-1 , nums , dp)

        ans = max(temp1 , temp2)
        dp[i] = ans
        return ans