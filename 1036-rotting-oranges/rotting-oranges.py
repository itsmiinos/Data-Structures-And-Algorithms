class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        my_queue = []
        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range (n) : 
            for j in range (m) : 
                if grid[i][j] == 2 : 
                    my_queue.append(Pair(i , j , 0))

        while len(my_queue) > 0  :
            temp = my_queue.pop(0)
            crow = temp.row
            ccol = temp.col
            ans = temp.time

            if crow-1 >= 0 and grid[crow-1][ccol] == 1 : 
                my_queue.append(Pair(crow-1 , ccol , ans+1))
                grid[crow-1][ccol] = 2
            if crow+1 <= n-1 and grid[crow+1][ccol] == 1 : 
                my_queue.append(Pair(crow+1 , ccol , ans+1)) 
                grid[crow+1][ccol] = 2
            if ccol-1 >= 0 and grid[crow][ccol-1] == 1 :
                my_queue.append(Pair(crow , ccol-1 , ans+1))
                grid[crow][ccol-1] = 2
            if ccol+1 <= m-1 and grid[crow][ccol+1] == 1 : 
                my_queue.append(Pair(crow , ccol + 1 , ans+1))
                grid[crow][ccol+1] = 2
            
        for i in range (n) : 
            for j in range (m) : 
                if grid[i][j] == 1 : 
                    return -1
        
        return ans


class Pair : 
    row = 0
    col = 0
    time = 0

    def __init__(self, r , c , t) : 
        self.row = r
        self.col = c
        self.time = t
