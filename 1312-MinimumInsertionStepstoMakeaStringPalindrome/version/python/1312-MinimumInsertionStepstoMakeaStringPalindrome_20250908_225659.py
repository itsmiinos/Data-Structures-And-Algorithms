# Last updated: 9/8/2025, 10:56:59 PM
class Solution:
    def minInsertions(self, s: str) -> int:
        t = s[::-1]
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]

        max_length = 0
        for i in range(1 , len(dp)) : 
            for j in range(1 , len(dp[i])) : 

                if s[i-1] == t[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(dp[i][j] , max_length)
                
                else : 
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return len(s) - max_length