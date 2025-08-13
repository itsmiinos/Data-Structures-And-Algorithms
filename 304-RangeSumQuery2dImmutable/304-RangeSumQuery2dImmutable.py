# Last updated: 8/13/2025, 8:20:09 PM
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n) : 
            self.prefixSum[i][0] = matrix[i][0]
        
        for i in range(n) : 
            for j in range(1, m) : 
                self.prefixSum[i][j] = self.prefixSum[i][j-1] + matrix[i][j]
        
        for j in range(m) : 
            for i in range(1,n) : 
                self.prefixSum[i][j] = self.prefixSum[i-1][j] + self.prefixSum[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.prefixSum[row2][col2]

        if row1-1 >= 0 : 
            sum = sum - self.prefixSum[row1-1][col2]

        if col1-1 >= 0 : 
            sum = sum - self.prefixSum[row2][col1-1]
        
        if row1-1 >= 0 and col1-1 >= 0 : 
            sum = sum + self.prefixSum[row1-1][col1-1]
        
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)