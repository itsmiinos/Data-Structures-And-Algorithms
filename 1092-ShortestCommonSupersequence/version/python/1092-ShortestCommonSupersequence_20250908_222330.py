# Last updated: 9/8/2025, 10:23:30 PM
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

        for i in range(1 , len(dp)) : 
            for j in range(1 , len(dp[i])) : 

                if str1[i-1] == str2[j-1] : 
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else : 
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        i = len(str1)
        j = len(str2)
        result = []

        while i > 0 and j > 0 : 
            if str1[i-1] == str2[j-1] :
                result.append(str1[i-1])
                i-=1
                j-=1
            
            else : 
                if dp[i][j-1] > dp[i-1][j] : 
                    result.append(str2[j-1])
                    j-=1
                
                else : 
                    result.append(str1[i-1])
                    i-=1
        
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        return ''.join(reversed(result))