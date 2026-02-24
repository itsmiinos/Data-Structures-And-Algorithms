# Last updated: 2/24/2026, 7:46:34 PM
1class Solution:
2    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
3        array = [[0 for _ in range(n)] for _ in range(n)]
4        for query in queries :
5            row1 , col1 , row2 , col2 = query
6            for i in range(row1 , row2 + 1) :
7                l = col1
8                r = col2
9                array[i][l] += 1
10                if r + 1 < n :
11                    array[i][r+1] -=1
12        
13
14        for i in range(n) :
15            for j in range(1 , n) :
16                array[i][j] += array[i][j-1]
17        
18
19        return array