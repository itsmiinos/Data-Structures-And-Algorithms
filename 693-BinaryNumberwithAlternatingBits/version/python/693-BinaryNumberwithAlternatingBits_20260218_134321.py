# Last updated: 2/18/2026, 1:43:21 PM
1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        x = n ^ (n >> 1)
4        return (x & (x + 1)) == 0
5        
6            
7
8