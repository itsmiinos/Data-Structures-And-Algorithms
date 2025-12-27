# Last updated: 12/28/2025, 2:46:07 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        ans = []
4        for i in range(32) :
5            ans.append((n>>i)&1)
6        
7        k = 31
8        number = 0
9        for i in range(len(ans)) :
10            number += (2 ** k) * ans[i]
11            k-=1
12        
13        return number
14