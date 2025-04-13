class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        

        while low <= high :
            mid = int(high + low / 2)
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                #discard left side
                low = mid+1
            elif nums[mid] > target :
                #discard right side
                high = mid-1
        
        return -1