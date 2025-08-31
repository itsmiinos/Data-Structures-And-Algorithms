#User function Template for python3
class Solution:
	def minDifference(self, nums):
		# code here
        total_sum = sum(nums)
        n = len(nums)

        dp = [[False for j in range(total_sum + 1)] for i in range(n)]
        
        # initialize
        for i in range(n):
            dp[i][0] = True   # sum = 0 always possible
        
        if nums[0] <= total_sum:
            dp[0][nums[0]] = True     
        
        # fill dp
        for i in range(1, n):
            for j in range(total_sum + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        half_sum = total_sum // 2
        min_diff = float("inf")

        for s in range(half_sum + 1):
            if dp[n-1][s]:
                min_diff = min(min_diff, total_sum - 2*s)

        return min_diff
