class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n) : 
            for j in range (i) : 

                #swap the values to get the transpose of the matrix

                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        #matrix is transposed, now time to rotate by reversing the rows

        for i in range(n) : 

            temp = matrix[i]
            temp.reverse()
        