# Last updated: 8/13/2025, 8:17:15 PM
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        M = 10**9 + 7
        while left <= right : 
            
            while right > -1 and nums[right] + nums[left] > target : 
                right-=1

            if nums[right] + nums[left] <= target : 
                ans = int(ans % M) + int(2**(right - left)%M)
                left+=1
        
        return ans