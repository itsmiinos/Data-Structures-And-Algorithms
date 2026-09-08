class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 1 2
        low = 0 
        high = len(nums) - 1
        ans = -1

        while low <= high : 
            mid = low + (high - low) // 2

            if nums[mid] > nums[high] :
                low = mid + 1
            
            else :
                if mid > 0 and nums[mid-1] > nums[mid] :
                    return nums[mid]
                else :
                    ans = mid
                    high = mid - 1
        
        return nums[ans]