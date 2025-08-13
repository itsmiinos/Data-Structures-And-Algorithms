# Last updated: 8/13/2025, 8:20:12 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1]*len(nums)
        # ans = 0

        # for i in range (len(nums)) :
        #     for j in range (i , -1 , -1) :
        #         if nums[i] > nums[j] :
        #             dp[i] = max(dp[i] , dp[j]+1)
        #     ans = max(ans , dp[i])
        # return ans

        dp = []  # This will store the smallest tail of increasing subsequences
        
        for num in nums:
            # Binary search for the first index in dp >= num
            lo, hi = 0, len(dp) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if dp[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            # If num is greater than all elements, append it
            if lo == len(dp):
                dp.append(num)
            else:
                dp[lo] = num  # Replace the first element >= num
        
        return len(dp)