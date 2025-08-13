# Last updated: 8/13/2025, 8:23:19 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        column_table = [0]*m
        row_table = [0]*n

        for i in range(n) : 
            for j in range(m) : 
                if matrix[i][j] == 0 :
                    row_table[i] = 1
                    column_table[j] = 1
        
        for i in range(n) : 
            for j in range(m) : 
                if row_table[i] == 1 or column_table[j] == 1 :
                    matrix[i][j] =0 


        