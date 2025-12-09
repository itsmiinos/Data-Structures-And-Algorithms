# Last updated: 12/9/2025, 10:43:27 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        dp = [-1]*(len(s)+1)
4        return self.solve(0 , s , dp)
5    
6    def solve(self , i : int , s : str , dp : list[int]) -> int : 
7        if i == len(s) : 
8            return 1
9        
10        if dp[i] != -1 : 
11            return dp[i]
12        
13        if s[i] == '0' : 
14            dp[i] = 0
15            return dp[i]
16
17        split = self.solve(i+1 , s , dp)
18        not_split = 0
19        if i+1 < len(s) :
20            if s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6) :
21                not_split = self.solve(i+2 , s , dp)
22        
23        dp[i] = split + not_split
24        return split + not_split