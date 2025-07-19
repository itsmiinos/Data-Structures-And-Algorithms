class Solution:
    def findFloor(self, arr, target):
        # code here

        low = 0
        high = len(arr)-1
        ans = -1
        while (low <= high) :
            mid = low + ((high - low) // 2)
            
            
            if arr[mid] <= target : 
                ans = mid
                low = mid + 1
            
            elif arr[mid] > target :
                
                high = mid - 1
            
            
        return ans
        