# Last updated: 12/2/2025, 8:31:26 PM
1class Node :
2    def __init__(self , val) :
3        self.val = val
4        self.isEnd = False
5        self.nextLetters = {}
6
7class Solution:
8    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
9        self.root = Node("")
10        result = set()
11
12        for i in range(len(words)) :
13            self.addWord(self.root , words[i])
14
15        for i in range(len(board)):
16            for j in range(len(board[i])) :
17                if board[i][j] in self.root.nextLetters :
18                    self.searchWord(self.root.nextLetters[board[i][j]] , board , i , j , board[i][j] , result)
19        
20        return list(result)
21    
22    def searchWord(self , root : 'Node' , board : list , i : int , j : int , temp : str , result : set) :
23        
24        if root.isEnd :
25            result.add(temp)
26
27        saved = board[i][j]
28        board[i][j] = '#'
29
30        directions = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]
31        for u , v in directions : 
32            ni , nj = i+u , j+v
33            if 0 <= ni <len(board) and 0 <= nj <len(board[0]) and board[ni][nj] in root.nextLetters :
34                self.searchWord(root.nextLetters[board[ni][nj]] , board , ni , nj , temp + board[ni][nj] , result)
35        
36        board[i][j] = saved
37
38        
39
40    def addWord(self , root : 'Node' , word : str) -> None :
41        curr = root
42        for i in range(len(word)):
43            if word[i] in curr.nextLetters :
44                curr = curr.nextLetters[word[i]]
45            else :
46                newNode = Node(word[i])
47                curr.nextLetters[word[i]] = newNode
48                curr = newNode
49        
50        curr.isEnd = True
51    