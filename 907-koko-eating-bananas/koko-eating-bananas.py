import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1

        while low <= high :
            mid = low + (high - low) // 2

            if self.eatPiles(piles , mid) <= h :
                ans = mid
                high = mid - 1
            
            else :
                low = mid + 1
        
        return ans
    
    def eatPiles(self , piles : list , n : int) -> int :

        count_hours = 0
        for i in range(len(piles)) :
            if n > piles[i] :
                count_hours +=1
            
            else :
                count_hours += math.ceil(piles[i] / n)
        
        return count_hours