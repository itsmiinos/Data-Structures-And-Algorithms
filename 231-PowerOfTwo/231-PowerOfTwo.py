# Last updated: 8/13/2025, 8:20:54 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 :
            return True
        
        elif n%2!=0 or n==0 :
            return False
        
        else :
            return self.isPowerOfTwo(n/2)
        
    
