# Last updated: 12/2/2025, 8:57:08 PM
1class Node :
2    def __init__(self , val) : 
3        self.val = val
4        self.isEnd = False
5        self.nextLetters = {}
6
7class WordDictionary:
8
9    def __init__(self):
10        self.root = Node("")
11
12    def addWord(self, word: str) -> None:
13        curr = self.root
14        for i in range(len(word)) : 
15            if word[i] in curr.nextLetters : 
16                curr = curr.nextLetters[word[i]]
17            else :
18                newNode = Node(word[i])
19                curr.nextLetters[word[i]] = newNode
20                curr = newNode
21        
22        curr.isEnd = True
23
24    def search(self, word: str) -> bool:
25
26        def dfs(idx , root) :
27            if idx == len(word) : 
28                return root.isEnd
29            
30            if word[idx] != "." :
31                if word[idx] in root.nextLetters :
32                    if dfs(idx + 1 , root.nextLetters[word[idx]]) : 
33                        return True
34            
35            else :
36                for curr in root.nextLetters.values() :
37                    if dfs(idx + 1 , curr) : 
38                        return True
39            
40            return False
41
42        return dfs(0 , self.root)
43
44
45# Your WordDictionary object will be instantiated and called as such:
46# obj = WordDictionary()
47# obj.addWord(word)
48# param_2 = obj.search(word)