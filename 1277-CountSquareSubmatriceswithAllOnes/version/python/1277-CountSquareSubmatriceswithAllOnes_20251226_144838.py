# Last updated: 12/26/2025, 2:48:38 PM
1class Solution:
2    def countSquares(self, matrix: List[List[int]]) -> int:
3        dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
4        for i in range(len(matrix)) :
5            dp[i][0] = matrix[i][0]
6        for j in range(len(matrix[0])) :
7            dp[0][j] = matrix[0][j]
8        
9        for i in range(1 , len(matrix)) :
10            for j in range(1 , len(matrix[0])) :
11                if matrix[i][j] == 0 :
12                    dp[i][j] = 0
13                else :
14                    dp[i][j] = 1 + min(dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1])
15        count = 0
16        for i in range(len(matrix)) :
17            for j in range(len(matrix[0])) :
18                count += dp[i][j]
19        
20        return count