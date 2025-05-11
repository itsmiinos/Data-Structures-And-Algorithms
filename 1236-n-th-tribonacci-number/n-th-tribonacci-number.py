class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1]*(n+1)
        result = self.tribonacciHelper(n , dp)
        return result
    
    def tribonacciHelper(self , n:[int] , dp:[int]) -> int:
        if n==0 or n==1 :
            return n
        if n==2 :
            return 1
        if dp[n] != -1 : return dp[n]
        a = self.tribonacciHelper(n-1,  dp)
        b = self.tribonacciHelper(n-2 , dp)
        c = self.tribonacciHelper(n-3 , dp)
        dp[n] = a+b+c
        return a+b+c