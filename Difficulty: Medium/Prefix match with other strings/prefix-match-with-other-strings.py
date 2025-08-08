#User function Template for python3

class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        if k > len(s) : 
            return 0
    
        self.createTrie()
        for i in range(len(arr)) : 
            self.insertTrie(arr[i])
        
        result = self.searchPrefix(s , k)
        
        return result
    
    def createTrie(self) :
        self.root = Node(0)
    
    def insertTrie(self , word : str) -> None : 
        t = self.root
        for i in range(len(word)) : 
            char = word[i]
            if char in t.hashmap : 
                t = t.hashmap[char]
                t.pc+=1
            else : 
                n = Node(1)
                t.hashmap[char] = n
                t = n
    
    def searchPrefix(self , s , k) -> int : 
        t = self.root
        i = 0
        count = 0
        while i < k :
            char = s[i]
            if char in t.hashmap : 
                t = t.hashmap[char]
                count = t.pc
            else : 
                return 0
            i+=1
        return count

class Node : 
    def __init__(self , pc) :
        self.pc = pc
        self.hashmap = {}