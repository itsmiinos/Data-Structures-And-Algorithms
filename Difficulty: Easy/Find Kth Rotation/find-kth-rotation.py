class Solution:
    def findKRotation(self, nums):
        # code here
        minnimum_index = 0
        low = 0
        high = len(nums)-1

        while low <= high : 
            mid = low + (high-low) // 2

            if nums[mid] < nums[high] : 
                if nums[minnimum_index] > nums[mid] : 
                    minnimum_index = mid
                high = mid-1
            
            else : 
                if nums[minnimum_index] > nums[low] : 
                    minnimum_index = low
                low = mid + 1
        
        return minnimum_index