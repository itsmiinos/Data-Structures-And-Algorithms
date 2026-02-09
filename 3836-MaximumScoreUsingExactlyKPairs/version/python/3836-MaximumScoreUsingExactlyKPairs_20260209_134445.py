# Last updated: 2/9/2026, 1:44:45 PM
1class Solution:
2    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
3        self.dp = {}
4        return self.solve(0 , 0, nums1 , nums2 , k)
5
6    
7    def solve(self , i : int , j : int  , nums1 : int , nums2 : int , k : int) -> int :
8        if k == 0:
9            return 0
10
11        if i == len(nums1) or j == len(nums2):
12            return float('-inf')
13        
14        if (i,  j , k) in self.dp :
15            return self.dp[(i , j , k)]
16    
17
18        skip_i = self.solve(i+1 , j , nums1 , nums2 , k)
19
20        skip_j = self.solve(i , j+1 , nums1 , nums2 , k )
21
22        take_both = (nums1[i] * nums2[j]) + self.solve(i+1 , j+1 , nums1 , nums2 , k-1)
23
24        ans = max(skip_i , skip_j , take_both)
25
26        self.dp[( i, j , k)] = ans
27        return ans