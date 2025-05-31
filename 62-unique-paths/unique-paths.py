class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range (n+1)] for _ in range(m+1)]
        result = self.uniquePathsHelper(m-1 , n-1 , dp)
        return result

    def uniquePathsHelper(self , i : int , j : int , dp : List[List[int]]) -> int : 
        if i  == 0 or j == 0 :
            return 1
        if dp[i][j] !=-1 : return dp[i][j]

        temp1 = self.uniquePathsHelper(i , j-1 , dp) 
        temp2 = self.uniquePathsHelper(i-1 , j , dp)
        dp[i][j] = temp1 + temp2
        return temp1 + temp2