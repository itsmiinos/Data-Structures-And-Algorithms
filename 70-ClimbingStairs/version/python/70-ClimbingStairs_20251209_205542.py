# Last updated: 12/9/2025, 8:55:42 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp1 = [-1]*(n+1)
4        dp2 = [-1]*(n+1)
5        return self.doDP(n , dp1)
6    
7    def doDP(self , n : int , dp : list) -> int : 
8        if n < 0 : 
9            return 0
10
11        if n == 0 : 
12            return 1
13
14        if dp[n] != -1 : 
15            return dp[n]
16        
17        one_step = self.doDP(n-1 , dp)
18        two_step = self.doDP(n-2 , dp)
19
20        dp[n] = one_step + two_step
21
22        return dp[n]
23
24