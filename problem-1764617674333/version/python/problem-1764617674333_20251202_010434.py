# Last updated: 12/2/2025, 1:04:34 AM
1class Node:
2    def __init__(self, value):
3        self.val = value
4        self.isEnd = False
5        self.nextLetters = {}
6
7class Solution:
8    def findWords(self, board, words):
9        self.root = Node("")
10        result = set()
11        m = len(board)
12        n = len(board[0])
13
14        # Build trie
15        for w in words:
16            self.addWord(self.root, w)
17
18        # DFS from every cell
19        for i in range(m):
20            for j in range(n):
21                ch = board[i][j]
22                if ch in self.root.nextLetters:
23                    self.checkWord(self.root.nextLetters[ch], board, i, j, ch, result)
24
25        return list(result)
26
27    # << FIXED: now returns boolean AND collects words properly >>
28    def checkWord(self, node, board, i, j, temp, result):
29        # If the node ends a word, collect it
30        if node.isEnd:
31            result.add(temp)
32
33        # Mark as visited
34        saved = board[i][j]
35        board[i][j] = "#"
36
37        directions = [[-1,0], [1,0], [0,-1], [0,1]]
38        
39        for u, v in directions:
40            ni, nj = i + u, j + v
41
42            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
43                ch = board[ni][nj]
44
45                if ch in node.nextLetters:
46                    self.checkWord(node.nextLetters[ch], board, ni, nj, temp + ch, result)
47
48        # Restore visited
49        board[i][j] = saved
50
51    def addWord(self, root, word):
52        curr = root
53        for ch in word:
54            if ch not in curr.nextLetters:
55                curr.nextLetters[ch] = Node(ch)
56            curr = curr.nextLetters[ch]
57        curr.isEnd = True
58