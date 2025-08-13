# Last updated: 8/13/2025, 8:19:31 PM
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for i in range(n)]
        result = self.lPSHelper(s , 0 , n-1 , dp)
        return result

    def lPSHelper(self , s : str , i : int , j : int , dp : [int]) -> int : 
        if i < 0 or j >= len(s) : 
            return 0
        if i > j : 
            return 0
        if i == j : 
            return 1
        if dp[i][j] !=-1 : return dp[i][j]
        
        if s[i] == s[j] : 
            dp[i][j] = 2 + self.lPSHelper(s , i+1 , j-1 , dp)
        else : 
            x = self.lPSHelper(s , i+1 , j , dp)
            y = self.lPSHelper(s , i , j-1 , dp)
            dp[i][j] = max(x,y)
        
        return dp[i][j]
            
