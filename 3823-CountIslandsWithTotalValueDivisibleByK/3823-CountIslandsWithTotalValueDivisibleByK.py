# Last updated: 8/13/2025, 8:14:47 PM
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visited = [[ False for j in range(len(grid[0]))] for i in range(len(grid))]
        my_queue = []

        n = len(grid)
        m = len(grid[0])

        for i in range(n) : 
            for j in range(m) : 
                if grid[i][j] > 0 : 
                    my_queue.append([i,j])
        count = 0
        while len(my_queue) > 0 : 
            popped = my_queue.pop(0)
            popped_row = popped[0]
            popped_col = popped[1]
            if visited[popped_row][popped_col] != True : 
                count += self.doBFSCheck(popped_row , popped_col , grid , k , visited)
            

        return count

    def doBFSCheck(self , row : int , col : int , grid : list[list[int]] , k : int , visited : list[list[bool]]) -> int : 
        queue = []
        sum = grid[row][col]
        n = len(grid)
        m = len(grid[0])
        visited[row][col] = True
        queue.append([row , col])

        while len(queue) > 0 : 
            popped = queue.pop(0)
            popped_row = popped[0]
            popped_col = popped[1]
            
            if popped_row - 1 >= 0 and grid[popped_row-1][popped_col] > 0 and visited[popped_row-1][popped_col] == False : 
                sum+=grid[popped_row-1][popped_col]
                visited[popped_row-1][popped_col] = True
                queue.append([popped_row-1 , popped_col])
    
            if popped_row + 1< n and grid[popped_row+1][popped_col] > 0 and visited[popped_row+1][popped_col] == False: 
                sum+=grid[popped_row+1][popped_col]
                visited[popped_row+1][popped_col] = True
                queue.append([popped_row+1 , popped_col])
    
            if popped_col - 1 >= 0 and grid[popped_row][popped_col-1] > 0 and visited[popped_row][popped_col-1] == False: 
                sum+=grid[popped_row][popped_col-1]
                visited[popped_row][popped_col-1] = True
                queue.append([popped_row , popped_col-1])

            if popped_col + 1 < m and grid[popped_row][popped_col+1] > 0 and visited[popped_row][popped_col+1] == False:
                sum+=grid[popped_row][popped_col+1]
                visited[popped_row][popped_col+1] = True
                queue.append([popped_row , popped_col+1])

        if sum % k == 0 : 
            return 1

        return 0
        