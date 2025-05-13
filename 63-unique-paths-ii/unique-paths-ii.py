class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1 for j in range (len(obstacleGrid[0]))] for i in range (len(obstacleGrid))]
        result = self.pathHelper(len(obstacleGrid)-1 , len(obstacleGrid[0])-1 , obstacleGrid , dp)
        return result

    def pathHelper(self , i:int , j : int , obstacleGrid : List[List[int]] , dp:List[List[int]]) -> int :
        if i==0 and j ==0 :
            return 1 if obstacleGrid[0][0] == 0 else 0
        if i<0 or j<0 or obstacleGrid[i][j] == 1 :
            return 0
        if dp[i][j] !=-1 : return dp[i][j]
        a = self.pathHelper(i , j-1 , obstacleGrid , dp)
        b = self.pathHelper(i-1 , j , obstacleGrid , dp)
        dp[i][j] = a+b
        return a+b