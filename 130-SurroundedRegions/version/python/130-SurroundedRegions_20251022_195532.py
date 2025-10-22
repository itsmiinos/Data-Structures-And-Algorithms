# Last updated: 10/22/2025, 7:55:32 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)) : 
            for j in range(len(board[0])) : 
                if (i == 0 or j == 0 or  i == len(board)-1 or j == len(board[0])-1) and board[i][j] == "O" :
                    if visited[i][j] == False : 
                        visited[i][j] = True
                        self.doBFS(i , j , visited , board)
        
        for i in range(len(board)):
            for j in range(len(board[0])) : 
                if board[i][j] == "O" and visited[i][j] == False : 
                    board[i][j] = "X"
        
    
    def doBFS(self , row : int , col : int , visited : int , board : int) -> None : 

        queue = []
        queue.append([row , col])
        

        while len(queue) > 0 : 
            row , col = queue.pop(0)
            

            if row-1 >= 0 and board[row-1][col] == "O" and visited[row-1][col] == False : 
                visited[row-1][col] = True
                queue.append([row-1,col])
            
            if row+1 < len(board) and board[row+1][col] == "O" and visited[row+1][col] == False : 
                visited[row+1][col] = True
                queue.append([row+1,col])
            
            if col-1 >= 0 and board[row][col-1] == "O" and visited[row][col-1] == False : 
                visited[row][col-1] = True
                queue.append([row, col-1])

            if col+1 < len(board[0]) and board[row][col+1] == "O" and visited[row][col+1] == False : 
                visited[row][col+1] = True
                queue.append([row , col+1])

