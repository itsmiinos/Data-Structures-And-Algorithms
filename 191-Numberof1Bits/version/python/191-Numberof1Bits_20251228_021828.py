# Last updated: 12/28/2025, 2:18:28 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        count = 0
4        for i in range(31 , -1 , -1) :
5            if (n >> i) & 1 :
6                count+=1
7        
8        return count