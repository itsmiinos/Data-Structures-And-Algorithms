# Last updated: 8/22/2025, 10:55:14 PM
class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:

        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)) :
            if i == 0 or i == len(board) - 1 : 
                for j in range(len(board[i])) : 
                    if board[i][j] == 1 :
                        self.doDFS( i , j , board , visited)

        for i in range(len(board)) :
            # if i == 0 or i == len(board) - 1 : 
            for j in range(len(board[i])) : 
                if j == 0 or j == len(board[i])-1 :
                    if board[i][j] == 1 :
                        self.doDFS( i , j , board , visited)
        count=0
        for i in range(len(board)) : 
            for j in range(len(board[i])) : 
                if board[i][j] == 1 and visited[i][j] == False : 
                    count+=1
        return count

    def doDFS(self , row : int , col : int , board : list[list[str]] , visited : list[bool]) -> None :

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return
        if visited[row][col] or board[row][col] != 1:
            return

        visited[row][col] = True
        nbrs = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]

        for n in nbrs : 
            if 0 <= row + n[0] < len(board) and 0 <= col + n[1] < len(board[0]) and board[row+n[0]][col+n[1]] == 1 :
                # visited[row+n[0]][col+n[1]] = True
                self.doDFS(row+n[0] , col+n[1] , board , visited)