# Last updated: 12/23/2025, 11:25:00 PM
1class Solution:
2    def cherryPickup(self, grid: List[List[int]]) -> int:
3        self.dp = {}
4        return self.helper(0 , 0 , len(grid[0])-1 , grid)
5
6    def helper(self , col1 : int  , row : int , col2 : int , grid : int) -> int :
7        if row == len(grid) :
8            return 0
9
10        if (row , col1 , col2) in self.dp :
11            return self.dp[(row , col1 , col2)]
12
13        directions = [ [1 , -1] , [1 , 0] , [1 , 1]]
14        ans = 0 
15        temp = 0
16
17        if col1 == col2 :
18            ans += grid[row][col1]
19        else :
20            ans += grid[row][col1] + grid[row][col2]
21
22        for _ , v in directions :
23            for _ , q in directions :
24                if 0 <= col1 + v < len(grid[0]) and 0 <= col2 + q < len(grid[0]) :
25                    temp = max(temp , self.helper(col1 + v , row + 1 , col2 + q , grid))
26        
27        self.dp[(row , col1 , col2)] = ans + temp
28
29        return self.dp[(row , col1 , col2)]
30
31
32
33        