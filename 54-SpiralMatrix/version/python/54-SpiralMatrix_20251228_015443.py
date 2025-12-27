# Last updated: 12/28/2025, 1:54:43 AM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        n = len(matrix) - 1
4        m = len(matrix[0]) - 1
5
6        step_row = n
7        step_col = m
8
9        i = 0
10        j = 0
11
12        ans = []
13
14        while step_row >=1 and step_col >= 1 :
15            for k in range(step_col) :
16                ans.append(matrix[i][j])
17                j+=1
18            
19            for k in range(step_row) :
20                ans.append(matrix[i][j])
21                i+=1
22            
23            for k in range(step_col , 0 , -1) :
24                ans.append(matrix[i][j])
25                j-=1
26            
27            for k in range(step_row , 0 , -1) :
28                ans.append(matrix[i][j])
29                i-=1
30        
31            step_row-=2
32            step_col-=2
33
34            i+=1
35            j+=1
36        
37        if step_row == 0 :
38            for k in range(step_col + 1) :
39                ans.append(matrix[i][j])
40                j+=1
41        
42        elif step_col == 0:
43            for k in range(step_row + 1) :
44                ans.append(matrix[i][j])
45                i+=1
46        
47        return ans