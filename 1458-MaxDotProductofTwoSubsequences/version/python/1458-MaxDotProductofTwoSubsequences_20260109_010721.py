# Last updated: 1/9/2026, 1:07:21 AM
1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        self.dp = [[-1 for _ in range(len(nums2))] for _ in range(len(nums1))]
4        return self.helper(nums1 , nums2 , 0 , 0)
5    
6    def helper(self , nums1 : list , nums2 : list , i : int , j : int) -> int :
7
8        if i == len(nums1) or j == len(nums2) :
9            return float('-inf')
10
11        if self.dp[i][j] != -1 : 
12            return self.dp[i][j]
13        
14        val = nums1[i] * nums2[j]
15
16        take1 = (nums1[i] * nums2[j]) + self.helper(nums1 , nums2 , i+1 , j+1)
17        take2 = self.helper(nums1 , nums2 , i , j+1)
18        take3 = self.helper(nums1 , nums2 , i+1 , j)
19
20        self.dp[i][j] = max(val , take1 , take2 , take3)
21
22        return self.dp[i][j]