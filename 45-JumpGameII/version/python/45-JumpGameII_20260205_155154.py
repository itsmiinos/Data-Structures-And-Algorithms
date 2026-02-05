# Last updated: 2/5/2026, 3:51:54 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        self.dp = [-1]*len(nums)
4        return self.solve(0 , nums)
5    
6    def solve(self , i : int , nums : list) -> list :
7        if i == len(nums)-1 :
8            return 0
9        
10        if nums[i] > len(nums)-1-i :
11            return 1
12
13        if self.dp[i] != -1 :
14            return self.dp[i]
15
16        min_steps = float('inf')
17        for k in range(nums[i] , 0 , -1) :
18            if i + k < len(nums):
19                min_steps = min(min_steps , 1 + self.solve(i+k , nums))
20        
21        self.dp[i] = min_steps
22        return self.dp[i]