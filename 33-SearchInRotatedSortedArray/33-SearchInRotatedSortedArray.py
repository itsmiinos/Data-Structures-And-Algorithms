# Last updated: 8/13/2025, 8:24:04 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1

        while low <= high : 
            mid = low + (high - low) // 2 

            if nums[mid] == target : 
                return mid
            
            elif nums[mid] <= nums[high] : 
                if target <= nums[high] and nums[mid] < target : 
                    low = mid + 1
                else : 
                    high = mid - 1

            elif nums[mid] > nums[high] : 
                if target >= nums[low] and nums[mid] > target : 
                    high = mid - 1
                else : 
                    low = mid + 1 
        
        return -1