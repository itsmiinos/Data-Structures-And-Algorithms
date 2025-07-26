class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 : 
            return 0
        
        if nums[0] > nums[1] : 
            return 0
        
        if nums[len(nums) - 1] > nums[len(nums) - 2] : 
            return len(nums) - 1
        
        low = 1
        high = len(nums)-2

        while low<=high : 
            mid = low+(high - low)//2 

            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid] : 
                return mid
            
            elif nums[mid-1] > nums[mid] : 
                high = mid-1
            
            else : 
                low = mid + 1
        
        return -1