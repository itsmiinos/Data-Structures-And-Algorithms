class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        ans = 0

        for i in range (len(nums)) :
            for j in range (i , -1 , -1) :
                if nums[i] > nums[j] :
                    dp[i] = max(dp[i] , dp[j]+1)
            ans = max(ans , dp[i])
        return ans