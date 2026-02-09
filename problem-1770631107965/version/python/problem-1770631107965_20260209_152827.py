# Last updated: 2/9/2026, 3:28:27 PM
1class Solution:
2    def countMonobit(self, n: int) -> int:
3        count = 1
4        for i in range(1 , n+1) :
5            if (i & (i + 1)) == 0 :
6                count +=1
7        
8        return count