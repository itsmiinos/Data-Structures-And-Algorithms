# Last updated: 8/13/2025, 8:24:33 PM
import sys
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0 
        p2 = len(height)-1
        max_water = -sys.maxsize

        while p1 < p2 : 

            water = (p2-p1) * min(height[p1] , height[p2])
            max_water = max(water , max_water)

            if height[p1] < height[p2] : 
                p1+=1
            else : 
                p2 -=1
        
        return max_water