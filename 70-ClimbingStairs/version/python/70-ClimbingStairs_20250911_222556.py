# Last updated: 9/11/2025, 10:25:56 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        result = self.helper(n , dp)
        return result

    def helper(self , i : int , dp : [int]) : 
        if i == 0 :
            return 1
        if i < 0 :
            return 0
        if dp[i] !=-1 : return dp[i]

        temp1 = self.helper(i-1 , dp)
        temp2 = self.helper(i-2 , dp)
        dp[i] = temp1 + temp2
        return temp1 + temp2