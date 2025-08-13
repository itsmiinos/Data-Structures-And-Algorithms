# Last updated: 8/13/2025, 8:23:16 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        low = 0 
        high = n-1

        while low <= high : 

            mid = low + (high - low) // 2

            if matrix[mid][0] > target : 
                high = mid - 1

            elif matrix[mid][m-1] < target : 
                low = mid + 1
            
            elif matrix[mid][0] <= target and matrix[mid][m-1] >= target : 
                
                l = 0
                h = m-1

                while l <= h : 
                    m = l + (h - l) // 2

                    if matrix[mid][m] == target : 
                        return True
                    
                    elif matrix[mid][m] < target : 
                        l = m + 1
                    
                    else : 
                        h = m - 1
                
                return False
            
        return False
