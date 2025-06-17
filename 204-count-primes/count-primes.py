import math
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0 
        if n<=2 : 
            return 0
        prime = [True]*(n)
        prime[0] = False
        prime[1] = False
        for i in range(2 , int(math.sqrt(n))+1) : 
            if prime[i] == True : 
                for j in range (i*i , n , i) : 
                    prime[j] = False
        
        for i in range(n) : 
            if prime[i] : 
                count+=1
        
        return count