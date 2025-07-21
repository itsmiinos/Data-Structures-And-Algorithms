class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        if len(nums) == 1 : 
            return nums[0]

        while low<=high : 
            mid = low + (high - low) // 2

            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]

            elif mid % 2 == 0 : 
                if nums[mid+1] == nums[mid] : 
                    low = mid + 1
                else : 
                    high = mid - 1
            else : 
                if nums[mid-1] == nums[mid] : 
                    low = mid + 1
                
                else : 
                    high = mid -1

        return -1