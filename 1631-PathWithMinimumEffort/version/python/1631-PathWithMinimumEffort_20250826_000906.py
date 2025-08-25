# Last updated: 8/26/2025, 12:09:06 AM
import heapq
class Pair :
    def __init__(self , row : int , col : int, height : int , height_diff : int) -> None : 
        self.row = row
        self.col = col
        self.height = height
        self.height_diff = height_diff
    
    def __lt__(self , other) :
        return self.height_diff < other.height_diff

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        visited = [[False for j in range(len(heights[0]))] for i in range(len(heights))]
        max_diff = float('-inf')
        
        heapq.heappush(heap , Pair(0 , 0 , heights[0][0] , 0))
        directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]

        while len(heap) > 0 :

            rem = heapq.heappop(heap)
            last_height = rem.height
            last_row = rem.row
            last_col = rem.col
            height_diff = rem.height_diff

            visited[last_row][last_col] = True

            max_diff = max(height_diff , max_diff)

            if last_row == len(heights) - 1 and last_col == len(heights[0]) - 1 : 
                return max_diff

            for r , c in directions : 
                if 0 <= last_row + r < len(heights) and 0<= last_col + c < len(heights[0]) and visited[last_row+r][last_col+c] == False:
                    h_diff = abs(last_height - (heights[last_row + r][last_col + c]))
                    heapq.heappush(heap , Pair(last_row + r , last_col + c , heights[last_row+r][last_col+c] , h_diff))
        
        return -1

            