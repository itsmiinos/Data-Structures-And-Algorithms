# Last updated: 2/4/2026, 2:59:21 PM
1class Solution:
2    def maxSumTrionic(self, nums: List[int]) -> int:
3        #[0,-2,-1,-3,0,2,-1]
4        self.dp = [[-1 for _ in range(4)] for _ in range(len(nums))]
5        return self.solve(0 , nums , 0)
6
7
8    def solve(self , i : int , nums : list , trend : int ) -> int :
9        if i == len(nums) :
10            # valid end only if fully trionic
11            return 0 if trend == 3 else float('-inf')
12        
13        if self.dp[i][trend] != -1 :
14            return self.dp[i][trend]
15
16        take = float('-inf')
17        skip = float('-inf')
18
19        if trend == 3 :
20            take = nums[i]
21
22        if i+1 < len(nums) :
23            if trend == 0 :
24                skip = self.solve(i+1 , nums , trend)
25                if i+1 < len(nums) and nums[i+1] > nums[i] :
26                    take = max(take , nums[i] + self.solve(i+1 , nums , 1))
27            elif trend == 1 : 
28                if nums[i+1] > nums [i] :
29                    take = max(take , nums[i] + self.solve(i+1 , nums , trend))
30                elif nums[i+1] < nums [i] :
31                    take = max(take , nums[i] + self.solve(i+1 , nums , 2))
32            elif trend == 2 :
33                if i+1 < len(nums) and nums[i+1] < nums[i] :
34                    take = max(take , nums[i] + self.solve(i+1 , nums , trend))
35                elif nums[i+1] > nums[i] :
36                    take = max(take , nums[i] + self.solve(i+1 , nums , 3))
37            elif trend == 3 :
38                if i+1 < len(nums) and nums[i+1] > nums[i] :
39                    take = max(take , nums[i] + self.solve(i+1 , nums , trend))
40
41        self.dp[i][trend] = max(take , skip)
42
43        return self.dp[i][trend]