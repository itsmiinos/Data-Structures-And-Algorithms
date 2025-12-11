# Last updated: 12/11/2025, 10:51:17 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        result = []
4        self.dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
5        for i in range(len(s)) : 
6            for j in range(i , len(s)) : 
7                if self.solve(s , i , j) : 
8                    result.append(s[i : j + 1])
9
10                
11        
12        return len(result)
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