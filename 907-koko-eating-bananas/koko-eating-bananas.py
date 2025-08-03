import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 #as koko can eat atleast 1 banana per hr
        high = 0 #sum of all the bananas in 1 hr

        for i in range(len(piles)) : 
            high = max(high , piles[i])
        
        result = self.doBinarySearch(low , high , piles , h)
        return result
    
    def doBinarySearch(self, low : int , high : int , piles : list[int] , h : int) -> int : 
        ans = float('inf')

        while low <= high : 
            mid = low + ((high - low) // 2)

            if self.calculateBananasEaten(mid , piles) <= h : 
                ans = mid
                high = mid - 1
            
            else : 
                low = mid + 1
        
        return ans
    
    def calculateBananasEaten(self , speed : int , piles : list[int]) -> int : 

        hour = 0
        for i in range(len(piles)) : 
            pile = piles[i]
            hour += math.ceil(pile / speed)
        
        return hour