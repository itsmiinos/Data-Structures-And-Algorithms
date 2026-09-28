class Solution:
    def maxDepth(self, s: str) -> int:
        i = 0
        count = 0
        max_count = 0
        while i < len(s) :
            if s[i] == "(" :
                count+=1
            elif s[i] == ")" :
                count -=1
            max_count = max(count , max_count)
            i+=1
        
        return max_count