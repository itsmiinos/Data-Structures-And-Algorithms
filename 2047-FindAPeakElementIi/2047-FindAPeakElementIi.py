# Last updated: 8/13/2025, 8:16:43 PM
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        
        low = 0
        high = m - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Find row with max element in mid column
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
                    
            left = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_row][mid + 1] if mid + 1 < m else -1
            curr = mat[max_row][mid]
            
            if curr > left and curr > right:
                return [max_row, mid]
            elif left > curr:
                high = mid - 1
            else:
                low = mid + 1
        
        return [-1, -1]
