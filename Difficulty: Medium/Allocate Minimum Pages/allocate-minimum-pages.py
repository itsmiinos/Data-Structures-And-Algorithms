class Solution:
    
    def findPages(self, arr, k):
        if len(arr) < k: 
            return -1
        
        low = max(arr)  # Start from max(arr)
        high = sum(arr)  # Max possible pages if one student takes all
        
        result = self.doBinarySearchOnAnswer(low, high, k, arr)
        return result
        
    def doBinarySearchOnAnswer(self, low: int, high: int, k: int, arr: [int]) -> int:
        ans = -1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
            if self.calculateStudentsFromPages(mid, arr) > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
            
        return ans
    
    def calculateStudentsFromPages(self, maxPages: int, arr: [int]) -> int:
        count = 1
        running_sum = 0
        
        for pages in arr:
            if running_sum + pages > maxPages:
                count += 1
                running_sum = pages
            else:
                running_sum += pages
        
        return count
