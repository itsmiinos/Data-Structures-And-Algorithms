# Last updated: 8/13/2025, 8:17:31 PM
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_divisor = -float('inf')

        for i in range(len(nums)) : 
            max_divisor = max(max_divisor , nums[i])
        
        result = self.doBinarySearch(1 , max_divisor , nums , threshold) 
        return result
    
    def doBinarySearch(self , low : int , high : int , nums : list[int] , threshold : int) -> int : 

        ans = 0 
        while low <= high : 
            mid = low + (high - low) // 2

            if self.calculateSum(mid , nums) <= threshold : 
                ans = mid
                high = mid - 1
            
            else : 
                low = mid + 1
        
        return ans

    def calculateSum(self , n : int , nums : list[int]) -> int : 

        sum = 0
        for i in range(len(nums)) : 
            sum += math.ceil(nums[i] / n)
        
        return sum
