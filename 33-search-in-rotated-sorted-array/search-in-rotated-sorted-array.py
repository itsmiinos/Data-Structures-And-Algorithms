class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high : 

            mid = low + (high - low) // 2

            if nums[mid] == target : 
                return mid

            elif nums[high] <= nums[mid] : 
                if target <= nums[mid] and target >= nums[low] : 
                    high = mid - 1
                
                else : 
                    low = mid + 1
            
            elif nums[high] > nums[mid] : 
                if target >= nums[mid] and target <= nums[high] : 
                    low = mid + 1
                
                else : 
                    high = mid - 1
            
        
        return -1