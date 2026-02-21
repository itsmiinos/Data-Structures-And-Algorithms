# Last updated: 2/21/2026, 1:10:09 PM
1import math
2class Solution:
3    def countPrimeSetBits(self, left: int, right: int) -> int:
4        ans = 0
5        for i in range(left, right + 1):
6            if self.isPrime(i.bit_count()):
7                ans += 1
8        return ans
9    
10    def isPrime(self , n : int) -> int :
11        if n < 2:
12            return False
13        for i in range(2, int(math.sqrt(n)) + 1):
14            if n % i == 0:
15                return False
16        return True