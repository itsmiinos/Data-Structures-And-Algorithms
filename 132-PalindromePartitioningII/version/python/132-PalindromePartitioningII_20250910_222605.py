# Last updated: 9/10/2025, 10:26:05 PM
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Precompute palindrome table
        pal = [[False]*n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i+1][j-1]

        # Step 2: DP array to store min cuts
        dp = [0]*n
        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float("inf")
                for j in range(i):
                    if pal[j+1][i]:
                        dp[i] = min(dp[i], dp[j]+1)

        return dp[n-1]
