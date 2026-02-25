# Last updated: 2/25/2026, 8:16:44 PM
1class Solution:
2    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
3        left = 0
4        right = len(queries)-1
5
6        ans = -1
7
8        if max(nums) == 0 :
9            return 0
10
11        while left <= right :
12            mid = left + (right - left) // 2
13            
14            if self.checkZeroArray(nums , mid , queries) == True :
15                ans = mid
16                right = mid-1
17            
18            else :
19                left = mid + 1
20            
21        return ans + 1 if ans != -1 else -1
22    
23    def checkZeroArray(self , nums : list[int] , n : int , queries : list[list[int]] ) -> bool :
24        diff = [0]*(len(nums) + 1)
25
26        for i in range(n+1) :
27            l , r , v = queries[i]
28            diff[l] +=v
29            diff[r+1] -=v
30            
31        for i in range(1 , len(diff)) :
32            diff[i] += diff[i-1]
33        
34        for i in range(len(nums)) :
35            if nums[i] > diff[i] :
36                return False
37        
38        return True