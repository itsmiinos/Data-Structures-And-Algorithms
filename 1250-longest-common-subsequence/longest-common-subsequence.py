class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[-1 for j in range(m)] for i in range(n)]
        result = self.lCSHelper(text1 , n-1 , text2 , m-1, dp)
        return result

    def lCSHelper(self , text1 : str , i : int , text2 : str , j:int , dp : List[List[int]]) -> int :
        if i<0 or j<0 : 
            return 0
        if dp[i][j] != -1 : return dp[i][j]

        if text1[i] == text2[j] :
            x = self.lCSHelper(text1 , i-1 , text2 , j-1 , dp)
            dp[i][j] = x+1
            return x + 1
        
        else : 
            x = self.lCSHelper(text1 , i-1 , text2 , j , dp) #exlcude char from text1
            y = self.lCSHelper(text1 , i , text2 , j-1 , dp) #exclude char from text2
            dp[i][j] = max(x,y)
            return max(x,y)