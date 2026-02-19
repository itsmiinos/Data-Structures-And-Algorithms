# Last updated: 2/19/2026, 8:29:22 PM
1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        prev = 0
4        curr = 1
5        result = 0
6
7        for i in range(1 , len(s)) :
8            if s[i] == s[i-1] :
9                curr +=1
10            else :
11                result += min(prev , curr)
12                prev = curr
13                curr = 1
14        
15        return result + min(prev , curr)