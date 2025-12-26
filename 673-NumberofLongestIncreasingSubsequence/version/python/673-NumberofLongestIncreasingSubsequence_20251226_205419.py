# Last updated: 12/26/2025, 8:54:19 PM
1class Solution:
2    def findNumberOfLIS(self, nums: List[int]) -> int:
3        dp = [1]*len(nums)
4        count = [1]*len(nums)
5        max_count = 0
6
7        for i in range(len(nums)) :
8            for j in range(i) :
9                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
10                    dp[i] = dp[j] + 1
11                    count[i] = count[j]
12                elif nums[j] < nums[i] and dp[j] + 1 == dp[i]:
13                    count[i] += count[j]
14            
15            max_count = max(max_count , dp[i])
16        c = 0
17        for i in range(len(dp)) :
18            if dp[i] == max_count : 
19                c +=count[i]
20        
21        return c