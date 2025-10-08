# Last updated: 10/8/2025, 10:18:36 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        ans = float('inf')
        while low<=high : 
            mid = low + (high - low) // 2

            if nums[mid] <= nums[high] : 
                ans = min(ans , nums[mid])
                high = mid - 1
            
            elif nums[mid] > nums[high] : 
                low = mid + 1
        
        return ans