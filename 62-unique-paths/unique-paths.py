class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for j in range(n)] for i in range(m)]
        result = self.helper(m-1 , n-1 , dp)
        return result

    def helper(self , i : int , j : int , dp : list[list[int]]) : 
        if i<0 or j<0 : 
            return 0
        if i == 0 and j == 0 : 
            return 1
        if dp[i][j] !=-1 : return dp[i][j]

        temp1 = self.helper(i-1 , j , dp)
        temp2 = self.helper(i , j-1 , dp) 

        dp[i][j] = temp1 + temp2
        return temp1 + temp2