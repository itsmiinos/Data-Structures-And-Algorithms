# Last updated: 10/10/2025, 8:51:09 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations) - 1

        while low <= high :
            mid = low + (high - low) // 2

            if citations[mid] == len(citations) - mid : 
                return citations[mid]
            
            elif citations[mid] < len(citations) - mid :
                low = mid + 1
            
            elif citations[mid] > len(citations) - mid : 
                high = mid - 1
        
        return len(citations) - low