# Last updated: 8/13/2025, 8:23:29 PM
import sys
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        result  = self.minPathSumHelper( grid , m-1 , n-1 , dp)
        return result

    def minPathSumHelper(self , grid : [int] , i : int, j : int , dp : list[list[int]]) :
        if i < 0 or j < 0 :
            return +sys.maxsize
        if i ==0 and j == 0 :
            return grid[i][j]
        if dp[i][j] !=-1 : return dp[i][j]

        temp1 = self.minPathSumHelper(grid , i-1 , j , dp) + grid[i][j]
        temp2 = self.minPathSumHelper(grid , i , j-1 , dp) + grid[i][j]

        dp[i][j] = min(temp1 , temp2)
        return dp[i][j]