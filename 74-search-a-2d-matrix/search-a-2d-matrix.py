class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_elements = len(matrix) * len(matrix[0])
        low = 0
        high = total_elements-1

        while low <= high :
            mid = low + (high - low) // 2 # 6

            row = (mid // len(matrix[0]))
            col = (mid % len(matrix[0]))

            
            if matrix[row][col] == target :
                return True
            
            elif matrix[row][col] < target :
                low = mid + 1
            
            else :
                high = mid - 1
        
        return False
