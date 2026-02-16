# Last updated: 2/16/2026, 12:01:26 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        num = 0
4        for i in range(31 , -1 , -1) :
5            if (n >> i) & 1 == 1 :
6                num += 2 ** (31 - i)
7        
8        return num