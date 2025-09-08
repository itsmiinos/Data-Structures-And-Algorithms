#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
		dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]

        max_length = 0
        for i in range(1 , len(dp)) : 
            for j in range(1 , len(dp[i])) : 

                if s[i-1] == s[j-1] and i != j : 
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(dp[i][j] , max_length)
                
                else : 
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return max_length