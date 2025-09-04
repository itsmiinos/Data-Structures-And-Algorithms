#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)

        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        max_length = 0
        for i in range(1 , len(dp)) : 
            for j in range(1, len(dp[i])) : 
                if s1[i-1] == s2[j-1] : 
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length , dp[i][j])
                else : 
                    dp[i][j] = 0

        return max_length