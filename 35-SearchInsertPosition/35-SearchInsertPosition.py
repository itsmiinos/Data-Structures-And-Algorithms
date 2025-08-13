# Last updated: 8/13/2025, 8:24:01 PM
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr)-1
        ans = 0
        while (low <= high) :
            mid = low + ((high - low) // 2)
            if arr[mid] == target : 
                return mid

            elif arr[mid] <= target :
                
                low = mid + 1
            
            elif arr[mid] > target :
                high = mid - 1

            
        return low