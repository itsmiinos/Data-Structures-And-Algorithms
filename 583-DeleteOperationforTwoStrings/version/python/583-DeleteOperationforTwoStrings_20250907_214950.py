# Last updated: 9/7/2025, 9:49:50 PM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for j in range(len(word2))] for i in range(len(word1))]
        result = self.calculateLCS(word1 , word2 , len(word1)-1 , len(word2)-1 , dp)
        return (len(word1) - result) + (len(word2) - result) 

    def calculateLCS(self , word1 : str , word2 : str , i : int , j : int , dp : list[list[int]]) -> int : 
        if i < 0 or j < 0 : 
            return 0
        
        if dp[i][j] != -1 : 
            return dp[i][j]

        if word1[i] == word2[j] :
            dp[i][j] =  self.calculateLCS(word1 , word2 , i-1 , j-1 , dp) + 1
            return dp[i][j]
        
        else : 
            dp[i][j] = max(self.calculateLCS(word1 , word2 , i-1 , j , dp) , self.calculateLCS(word1 , word2 , i , j-1 , dp))
            return dp[i][j]
    