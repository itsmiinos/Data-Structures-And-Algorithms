# Last updated: 8/13/2025, 8:18:05 PM
class Solution(object):
    def fib(self, n):
        if n==0 or n==1 :
            return n
        a = self.fib(n-1)
        b = self.fib(n-2)
        return a + b