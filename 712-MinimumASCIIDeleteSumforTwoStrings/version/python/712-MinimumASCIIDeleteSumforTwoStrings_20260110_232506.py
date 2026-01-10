# Last updated: 1/10/2026, 11:25:06 PM
1class Solution:
2    def minimumDeleteSum(self, s1: str, s2: str) -> int:
3        self.dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
4        return self.solve(s1 , s2 , 0 , 0)
5
6    def solve(self , s1 : str , s2 : str , i : int  , j : int) -> int : 
7        if i == len(s1):
8            return sum(ord(c) for c in s2[j:])
9        if j == len(s2):
10            return sum(ord(c) for c in s1[i:])
11        
12        if self.dp[i][j] != -1 : 
13            return self.dp[i][j]
14        
15        if s1[i] == s2[j] :
16            self.dp[i][j] =  self.solve(s1 , s2 , i+1 , j+1)
17        
18        else :
19            self.dp[i][j] = min(ord(s1[i]) + self.solve(s1 , s2 , i+1 , j) , 
20                ord(s2[j]) + self.solve(s1 , s2 , i , j+1) ,
21                ord(s1[i]) + ord(s2[j]) + self.solve(s1 , s2 , i+1 , j)
22            )
23        
24        return self.dp[i][j]
25        
26