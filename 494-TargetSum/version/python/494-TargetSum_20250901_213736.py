# Last updated: 9/1/2025, 9:37:36 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = 0

        for i in range(len(nums)) : 
            total_sum += nums[i]
        
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0

        required_sum = (total_sum + target) // 2
        
        dp = [[0 for j in range(required_sum+1)] for i in range(len(nums))]
    
        for i in range(len(dp)) : 
            dp[i][0] = 1
        
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            if nums[0] <= required_sum:
                dp[0][nums[0]] = 1
        
        for i in range(1 , len(dp)) : 
            for j in range(len(dp[i])) : 
                if nums[i] <= j : 
                    a = dp[i-1][j-nums[i]]
                    b = dp[i-1][j]
                    dp[i][j] = a + b
                
                else : 
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(nums)-1][required_sum]
        
