# Last updated: 12/5/2025, 10:10:15 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        for i in range(len(board)) : 
4            for j in range(len(board[i])) : 
5                if board[i][j] == word[0] and self.helper(board , i , j , word , 1) : 
6                    return True
7        return False
8
9    def helper(self , board : list , i : int , j : int , word : str , index : int) -> bool :
10
11        if index > len(word) - 1: 
12            return True
13        
14        saved = board[i][j]
15        board[i][j] = "#"
16
17        directions = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]
18
19        for u , v in directions : 
20            ni = i + u
21            nj = j + v
22
23            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and word[index] == board[ni][nj] : 
24                if self.helper(board , ni , nj , word , index + 1) :
25                    return True
26                    
27        
28        board[i][j] = saved
29
30        return False
31        
32