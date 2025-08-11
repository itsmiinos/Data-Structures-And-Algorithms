#User function Template for python3
class Node : 
    def __init__(self) : 
        self.hashmap = [None , None]
        
class Solution:
    def maxXor(self, nums):
        #code here
        self.root = Node()
        
        max_number = float('-inf')
        for i in range(len(nums)) : 
            max_number = max(max_number , nums[i])

        self.max_set_bit = 0
        for i in range(31 , -1 , -1) :
            if max_number & (1 << i) : 
                self.max_set_bit = i
                break

        for i in range(len(nums)) : 
            self.insertIntoTrie(self.root , nums[i])

        max_xor = 0
        for i in range(len(nums)) : 
            max_xor = max(max_xor , self.searchOppositeParity(self.root , nums[i]) ^ nums[i])
        
        return max_xor
    
    def insertIntoTrie(self , root : Node , n : int) -> None : 
        t = root

        for i in range(self.max_set_bit , -1 , -1) : 
            ch = self.checkBit(n , i)

            if t.hashmap[ch] : 
                t = t.hashmap[ch]
            else : 
                n1 = Node()
                t.hashmap[ch] = n1
                t = n1
        
    def searchOppositeParity(self , root : Node , n : int) -> int : 

        t = root
        number = 0
        for i in range(self.max_set_bit , -1 , -1) : 
            ch = 1 - self.checkBit(n,i)

            if t.hashmap[ch] : 
                number = number + ( (2 ** i) * ch)
                t = t.hashmap[ch]
            else : 
                number = number + ( (2 ** i) * (1-ch))
                t = t.hashmap[1 - ch]
        
        return number
    
    def checkBit(self , n : int  , i : int) -> int : 
        if n & (1 << i) : 
            return 1
        else : 
            return 0