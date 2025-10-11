# Last updated: 10/11/2025, 9:32:48 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = []
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)) : 
            for j in range(len(grid[i])) : 
                if grid[i][j] == 1 : 
                    queue.append([i , j])
                    visited[i][j] = 1
                    break

        perimeter = 0
        
        directions = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]
        while len(queue) > 0 : 
            rem = queue.pop(0)
            row = rem[0]
            col = rem[1]

            for i in range(len(directions)) : 
                if 0 <= row + directions[i][0] < len(grid) and 0 <= col + directions[i][1] < len(grid[0]):
                    if grid[row + directions[i][0]][col + directions[i][1]] == 1 :
                        if visited[row + directions[i][0]][col + directions[i][1]]!=1 :
                            queue.append([row + directions[i][0] , col + directions[i][1]])
                            visited[row + directions[i][0]][col + directions[i][1]] = 1
                    else : 
                        perimeter +=1
                else : 
                    perimeter+=1
        
        
        return perimeter