class Solution:
    
    ''' n : int
        k : int
        Return Type : Boolean '''
    def checkKthBit(self, n, k):
        # Your code here
        if n & (1<<k) : 
            return True
        return False
        