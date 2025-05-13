class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for j in range(m)] for i in range(n)]
        result = self.pathHelper(n-1 , m-1 , grid , dp)
        return result

    def pathHelper(self , i:int , j : int , grid : List[List[int]] , dp : List[List[int]]) -> int :
        if i ==0 and j ==0 :
            return grid[i][j]
        if i<0 or j < 0 :
             return float('inf')
        if dp[i][j] !=-1 : return dp[i][j] 
        a = self.pathHelper(i , j-1 , grid , dp) + grid[i][j] # left -> right
        b = self.pathHelper(i-1 , j , grid , dp) + grid[i][j] # top -> bottom
        dp[i][j] = min(a,b)
        return min(a,b)