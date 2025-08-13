# Last updated: 8/13/2025, 8:15:26 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(1,len(s)):
            res += abs(ord(s[i-1]) - ord(s[i]))
        
        return res