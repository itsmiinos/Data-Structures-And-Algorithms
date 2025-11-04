# Last updated: 11/4/2025, 10:52:40 PM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        return self.solve(len(word1)-1 , len(word2)-1 , word1 , word2 , dp)
    
    def solve(self , i : int , j : int , s : str , t : str , dp : int) -> int :
        if j < 0 : 
            return i + 1
        
        if i < 0 : 
            return j + 1

        if dp[i][j] != -1 : 
            return dp[i][j]
        
        if s[i] == t[j] : 
            dp[i][j] = self.solve(i-1 , j-1 , s , t , dp)
            return dp[i][j]
        else : 
            replace = self.solve(i-1 , j-1 , s , t , dp) + 1
            insert = self.solve(i , j-1 , s , t , dp) + 1
            delete = self.solve(i-1 , j , s , t , dp) + 1
            dp[i][j] = min(replace , insert , delete)
            return dp[i][j]