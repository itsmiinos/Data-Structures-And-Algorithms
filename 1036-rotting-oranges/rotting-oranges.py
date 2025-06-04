class Pair : 
    row = 0
    col = 0
    t = 0
    def __init__(self , i : int , j : int , t : int) :
        self.row = i
        self.col = j
        self.t = t 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        my_queue = []
        ans = 0

        for i in range (n) : 
            for j in range (m) : 
                if grid[i][j] == 2 : 
                    my_queue.append(Pair(i , j , 0))
        
        while len(my_queue) > 0 : 
            temp = my_queue.pop(0)
            crow = temp.row
            ccol = temp.col
            ans = temp.t

            if crow-1 >= 0 and grid[crow-1][ccol] == 1 : 
                my_queue.append(Pair(crow-1 , ccol , temp.t+1))
                grid[crow-1][ccol] = 2
            
            if crow+1 < len(grid) and grid[crow+1][ccol] == 1 : 
                my_queue.append(Pair(crow+1 , ccol , temp.t+1))
                grid[crow+1][ccol] = 2
            
            if ccol+1 < len(grid[0]) and grid[crow][ccol+1] == 1 : 
                my_queue.append(Pair(crow , ccol+1 , temp.t+1))
                grid[crow][ccol+1] = 2
            
            if ccol-1 >=0 and grid[crow][ccol-1] == 1 : 
                my_queue.append(Pair(crow , ccol-1 , temp.t+1))
                grid[crow][ccol-1] = 2
            
        for i in range (n) : 
            for j in range (m) : 
                if grid[i][j] == 1 : 
                    return -1
        
        return ans
            