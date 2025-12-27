# Last updated: 12/28/2025, 2:31:21 AM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = []
4        for i in range(n+1) :
5            ans.append(self.hammingWeight(i))
6        
7        return ans
8    
9    def hammingWeight(self, n: int) -> int:
10        count = 0
11        for i in range(31 , -1 , -1) :
12            if (n >> i) & 1 :
13                count+=1
14        
15        return count