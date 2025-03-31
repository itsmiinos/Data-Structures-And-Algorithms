class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
        if n ==0 :
            return 1
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            half = self.myPow(x, (n - 1) // 2)
            return x * half * half
        