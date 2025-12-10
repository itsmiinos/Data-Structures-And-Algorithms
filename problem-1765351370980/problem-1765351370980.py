# Last updated: 12/10/2025, 12:52:50 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        dp = [-1]*(len(s)+1)
4        return self.helper( 0 , len(s) , s , dp)
5    
6    def helper(self , i : int , n : int , s  : int, dp : list) -> int :
7        if i == n : 
8            return 1
9        
10        if s[i] == '0' :
11            dp[i] = 0
12            return dp[i]
13        
14        if dp[i] != -1 : 
15            return dp[i]
16
17        split = self.helper(i+1 , n , s , dp)
18        not_split = 0
19        if i+1 < n :
20            if s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6) : 
21                not_split = self.helper(i+2 , n , s , dp)
22
23        dp[i] = split + not_split
24        return dp[i] 