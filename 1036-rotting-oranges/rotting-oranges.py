class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        my_queue = []
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == 2 :
                    my_queue.append([i,j,0])
        
        while len(my_queue) > 0 : 
            popped = my_queue.pop(0)
            curr_row = popped[0]
            curr_col = popped[1]
            ans = popped[2]

            if curr_row - 1 >= 0 and grid[curr_row-1][curr_col] == 1 : 
                grid[curr_row - 1][curr_col] = 2
                my_queue.append([curr_row-1 , curr_col , ans + 1])
            
            if curr_row + 1 < n and grid[curr_row+1][curr_col] == 1 : 
                grid[curr_row + 1][curr_col] = 2
                my_queue.append([curr_row+1 , curr_col , ans + 1])
            
            if curr_col - 1 >= 0 and grid[curr_row][curr_col - 1] == 1 : 
                grid[curr_row][curr_col-1] = 2
                my_queue.append([curr_row , curr_col-1 , ans +1])
            
            if curr_col + 1 < m and grid[curr_row][curr_col + 1]  == 1 : 
                grid[curr_row][curr_col+1] = 2
                my_queue.append([curr_row , curr_col+1 , ans +1])
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) : 
                if grid[i][j] == 1 : 
                    return -1

        return ans

