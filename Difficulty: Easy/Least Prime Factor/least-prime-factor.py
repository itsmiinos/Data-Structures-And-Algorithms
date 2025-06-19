#User function Template for python3
import math
class Solution:
    def leastPrimeFactor (self, n):
        # code here 
        spf = [-1]*(n+1)
        
        for i in range(n+1) : 
            spf[i] = i
        
        spf[0] = 0
        spf[1] = 1
        
        for i in range(2 , int(math.sqrt(n)+1)) : 
            for j in range(i*i , n+1 , i) : 
                spf[j] = min(spf[j] , i)
                
        return spf
            