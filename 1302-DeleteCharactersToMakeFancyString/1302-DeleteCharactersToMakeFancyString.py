# Last updated: 8/13/2025, 8:17:39 PM
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0 : 2]
        k = 2
        for i in range(2 , len(s)) : 
            if s[i] != result[k-1] or s[i] != result[k-2] : 
                result+=s[i]
                k+=1
        return result