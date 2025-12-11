# Last updated: 12/11/2025, 10:44:38 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        maxLength = 0
4        start = -1
5        self.dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
6        for i in range(len(s)) : 
7            for j in range(i , len(s)) : 
8                if self.solve(s , i , j) and j-i+1 > maxLength : 
9                    maxLength = max(maxLength , j - i + 1)
10                    start = i
11        
12        return s[start : start + maxLength]
13    
14    def solve(self , s , start , end) :
15        if start >= end : 
16            return True
17        
18        if self.dp[start][end] != -1 : 
19            return self.dp[start][end]        
20
21        if s[start] == s[end] : 
22            self.dp[start][end] = self.solve(s , start + 1 , end-1)
23            return self.dp[start][end]
24
25        self.dp[start][end] = False
26        
27        return self.dp[start][end]
28            