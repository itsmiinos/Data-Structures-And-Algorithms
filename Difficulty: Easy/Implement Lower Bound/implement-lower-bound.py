class Solution:
    def lowerBound(self, arr, target):
        #code here
        
        low = 0
        high = len(arr)-1
        ans = len(arr)
        while (low <= high) :
            mid = low + ((high - low) // 2)
            
            if arr[mid] < target : 
                low = mid + 1
            
            elif arr[mid] >= target :
                ans = min(mid , ans)
                high = mid - 1
            
            
        return ans