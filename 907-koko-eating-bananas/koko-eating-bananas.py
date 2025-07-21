import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = -float('inf')

        for i in range(len(piles)) : 
            max_bananas = max(max_bananas , piles[i])

        result = self.doBinarySearch(1 , max_bananas , piles , h)
        return result
    
    def doBinarySearch(self , low : int , high : int , piles : list[int] , h : int) -> int : 
        ans = 0
        while low <= high : 

            mid = low + (high - low) // 2

            if self.calculateHours(mid , piles) > h : 
                low = mid + 1
            
            else : 
                ans = mid
                high = mid - 1
        
        return ans
    
    def calculateHours(self , speed : int , piles : list[int]) -> int : 
        time = 0
        for i in range(len(piles)) : 
            time += math.ceil(piles[i] / speed)
        
        return time
