# Last updated: 8/13/2025, 8:20:19 PM
import math , sys
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1]*(n+1)
        result = self.numSquareHelper(n , dp , sys.maxsize)
        return result

    def numSquareHelper(self , n : int , dp : [int] , result) :
        if n == 0 or n == 1 : 
            return n
        if dp[n] !=-1 : return dp[n]
        for i in range (1 , int(math.sqrt(n)) + 1) : 
            square = 1 + self.numSquareHelper(n - i*i , dp , result)
            result = min(square , result)
        dp[n] = result
        return result
        