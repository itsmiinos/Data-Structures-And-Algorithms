# Last updated: 12/12/2025, 11:20:48 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        self.maxLength = 0
4        self.st = -1
5        if len(s) <= 1 : 
6            return s
7        for i in range(1 , len(s)) : 
8            self.doDP(i , i , s)
9            self.doDP(i-1 , i  , s)
10        
11        return s[self.st : self.st + self.maxLength]
12    
13
14    def doDP(self , start : int , end : int , s : str) -> None : 
15
16        if start < 0 or end > len(s)-1 : 
17            return
18        
19        if s[start] == s[end] :
20            if end - start + 1 > self.maxLength :
21                self.maxLength = max(self.maxLength , end - start + 1)
22                self.st= start
23            self.doDP(start - 1  , end + 1 , s)
24        
25        else : 
26            return
27        