# Last updated: 12/28/2025, 2:02:08 AM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        zero_row = set()
7        zero_col = set()
8
9        for i in range(len(matrix)) :
10            for j in range(len(matrix[i])) :
11                if matrix[i][j] == 0 :
12                    zero_row.add(i)
13                    zero_col.add(j)
14
15
16        for i in range(len(matrix)) :
17            for j in range(len(matrix[i])) :
18                if i in zero_row or j in zero_col :
19                    matrix[i][j] = 0
20        
21        