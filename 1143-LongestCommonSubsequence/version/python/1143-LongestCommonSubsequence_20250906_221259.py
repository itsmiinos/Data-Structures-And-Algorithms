# Last updated: 9/6/2025, 10:12:59 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0 for j in range(m+1)] for i in range(n+1)]

        for i in range(1 , len(dp)) : 
            for j in range(1, len(dp[i])) : 
                if text1[i-1] == text2[j-1] : 
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else : 
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

        return dp[n][m]