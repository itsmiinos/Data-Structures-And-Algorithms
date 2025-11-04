# Last updated: 11/4/2025, 10:31:59 PM
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
        return self.solve(len(s)-1 , len(t)-1 , s , t , dp)
    
    def solve(self , i : int , j : int , s : str , t : str , dp : int) -> int :
        if j < 0 : 
            return 1
        
        if i < 0 : 
            return 0

        if dp[i][j] != -1 : 
            return dp[i][j]
        
        if s[i] == t[j] : 
            dp[i][j] = self.solve(i-1 , j-1 , s , t , dp) + self.solve(i-1 , j , s , t ,dp)
            return dp[i][j]
        else : 
            dp[i][j] = self.solve(i-1 , j , s , t, dp)
            return dp[i][j]