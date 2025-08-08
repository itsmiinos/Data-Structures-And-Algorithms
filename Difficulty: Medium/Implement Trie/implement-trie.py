#User function Template for python3
class Trie:
    def __init__(self):
        # implement Trie
        self.root = Node(" ")
        
    def insert(self, word: str):
       # insert word into Trie
        t = self.root
        for i in range(len(word)) : 
            char = word[i]
            if char in t.hashmap : 
               t = t.hashmap[char]
            else : 
                n1 = Node(char)
                t.hashmap[char] = n1
                t = n1
        
        t.eow = True

    def search(self, word: str) -> bool:
         # search word in the Trie
        t = self.root
        for i in range(len(word)) : 
            char = word[i]
            if char in t.hashmap : 
                t = t.hashmap[char]
            else : 
                return False
        
        return t.eow

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
        t = self.root
        for i in range(len(word)) : 
            char = word[i]
            if char in t.hashmap : 
                t = t.hashmap[char]
            else : 
                return False
        
        return True
         
class Node  : 
    def __init__(self, value) : 
        self.val = value
        self.hashmap = {}
        self.eow = False