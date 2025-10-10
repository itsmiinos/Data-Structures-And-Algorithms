# Last updated: 10/10/2025, 9:07:04 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high : 

            mid = low + (high - low) // 2
            
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid  # Peak lies on the left or is mid itself

        return low