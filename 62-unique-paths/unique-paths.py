class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        result = self.pathHelper(m-1,n-1,dp)
        return result
    
    def pathHelper(self , i:int , j:int , dp:[int]) -> int :
        if i==0 or j==0 :
            return 1
        if dp[i][j] !=-1 : return dp[i][j]
        a = self.pathHelper(i-1 , j , dp)
        b = self.pathHelper(i, j -1 , dp)
        dp[i][j] = a+b
        return a+b