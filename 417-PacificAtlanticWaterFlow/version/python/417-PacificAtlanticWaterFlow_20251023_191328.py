# Last updated: 10/23/2025, 7:13:28 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific_visited = [[False for _ in range(m)] for _ in range(n)]
        atlantic_visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(m) : 
            self.doDFS(0 , i , heights , pacific_visited)
            self.doDFS(n-1 , i , heights , atlantic_visited)

        for i in range(n) : 
            self.doDFS(i , m-1 , heights , atlantic_visited)
            self.doDFS(i , 0 , heights , pacific_visited)

        result = []

        for i in range(n) : 
            for j in range(m) : 
                if atlantic_visited[i][j] == pacific_visited[i][j] == True : 
                    result.append([i,j])
        
        return result
        
    def doDFS(self , row : int , col : int , heights : list[list[int]] , visited : list[list[bool]]) -> None : 

        if (row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0])) or visited[row][col] == True : 
            return 
        
        visited[row][col] = True
        
        directions = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]

        for r , c in directions : 
            if (0 <= (row + r) < len(heights) and 0 <= (col + c) < len(heights[0])) and heights[row+r][col+c] >= heights[row][col] and visited[row+r][col+c] == False : 
                self.doDFS(row+r , col+c , heights , visited)
        