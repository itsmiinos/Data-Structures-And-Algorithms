# Last updated: 12/21/2025, 8:48:49 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        # dp = [-1] * (n)
4        # return self.helper(n-1 , dp) + self.helper(n-2 , dp)
5        if n == 1 or n == 2 : 
6            return n
7
8        dp = [-1] * (n + 1)
9        dp[0] = 0
10        dp[1] = 1
11        dp[2] = 2
12
13        for i in range(3 , n+1) :
14            dp[i] = dp[i-1] + dp[i-2]
15        
16        return dp[n]
17
18    def helper(self , n : int , dp : list ) -> int :
19        if n == 0 : 
20            return 1
21
22        if n < 0 : 
23            return 0
24
25        if dp[n] != -1:
26            return dp[n]
27        
28        one_step = self.helper(n-1 , dp)
29        two_step = self.helper(n-2 , dp)
30
31        dp[n] = one_step + two_step
32
33        return one_step + two_step