class Solution:
    def findMin(self, nums: List[int]) -> int:
        minnimum = float('inf')
        low = 0
        high = len(nums)-1

        while low <= high : 
            mid = low + (high-low) // 2

            if nums[mid] < nums[high] : 
                minnimum = min(minnimum , nums[mid])
                high = mid-1
            
            else : 
                minnimum = min(minnimum , nums[low])
                low = mid + 1
        
        return minnimum