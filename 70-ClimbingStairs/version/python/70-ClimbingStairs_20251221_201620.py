# Last updated: 12/21/2025, 8:16:20 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp = [-1] * (n)
4        return self.helper(n-1 , dp) + self.helper(n-2 , dp)
5
6    def helper(self , n : int , dp : list ) -> int :
7        if n == 0 : 
8            return 1
9
10        if n < 0 : 
11            return 0
12
13        if dp[n] != -1:
14            return dp[n]
15        
16        one_step = self.helper(n-1 , dp)
17        two_step = self.helper(n-2 , dp)
18
19        dp[n] = one_step + two_step
20
21        return one_step + two_step