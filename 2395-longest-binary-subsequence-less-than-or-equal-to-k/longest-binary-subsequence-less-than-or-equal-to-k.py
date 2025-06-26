class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        length = 0
        power = 1
        for i in reversed(s) : 
            if i == '0' : 
                length +=1
                power = power * 2
            else : 
                if power <= k and int(i) * power <= k : 
                    k = k - int(i) * power
                    length+=1
                    power = power * 2
                
        
        return length

              
