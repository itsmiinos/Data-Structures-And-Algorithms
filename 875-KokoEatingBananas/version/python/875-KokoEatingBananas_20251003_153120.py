# Last updated: 10/3/2025, 3:31:20 PM
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = 0

        for i in range(len(piles)) : 
            max_speed += piles[i]
        

        result = self.doBinarySearch(min_speed , max_speed , piles , h)
        return result

    def doBinarySearch(self , min_speed : int , max_speed : int , piles : list[int] , h : int) -> int : 

        low = min_speed
        high = max_speed
        ans = float('inf')
    
        while low <= high : 

            mid = low + ((high - low) // 2)

            if self.calculateTimeTaken(mid , piles) > h : 
                low = mid + 1
            
            elif self.calculateTimeTaken(mid , piles) <= h : 
                ans = min(ans , mid)
                high = mid - 1
        
        return ans
    
    def calculateTimeTaken(self , speed : int , piles : list[int]) -> int :

        total_time = 0

        for i in range(len(piles)) : 
            total_time += math.ceil(piles[i] / speed)
        
        return total_time
                