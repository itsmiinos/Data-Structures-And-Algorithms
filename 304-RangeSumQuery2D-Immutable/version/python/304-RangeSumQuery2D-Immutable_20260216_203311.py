# Last updated: 2/16/2026, 8:33:11 PM
1class NumMatrix:
2
3    def __init__(self, matrix: List[List[int]]):
4        m = len(matrix)
5        n = len(matrix[0])
6
7        prefix_array = [[-1 for _ in range(n)] for _ in range(m)]
8
9        for i in range(m) :
10            prefix_array[i][0] = matrix[i][0]
11
12        for i in range(m) :
13            for j in range (1 , n) :
14                prefix_array[i][j] = prefix_array[i][j-1] + matrix[i][j]
15            
16        for i in range(1 , m) :
17            for j in range(n) :
18                prefix_array[i][j] = prefix_array[i-1][j] + prefix_array[i][j]
19        
20        self.array = prefix_array
21
22    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
23        
24        sum = self.array[row2][col2]
25
26        if col1 - 1 >= 0 :
27            sum -= self.array[row2][col1 - 1]
28        
29        if row1 - 1 >= 0 :
30            sum -= self.array[row1 - 1][col2]
31        
32        if row1 - 1 >= 0 and col1 - 1 >= 0 :
33            sum += self.array[row1 - 1][col1 - 1]
34        
35        return sum
36
37
38# Your NumMatrix object will be instantiated and called as such:
39# obj = NumMatrix(matrix)
40# param_1 = obj.sumRegion(row1,col1,row2,col2)