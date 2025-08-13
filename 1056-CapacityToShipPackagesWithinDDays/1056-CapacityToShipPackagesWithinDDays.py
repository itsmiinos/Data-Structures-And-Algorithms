# Last updated: 8/13/2025, 8:18:02 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = -float('inf')
        max_cap = 0

        for i in range(len(weights)) : 
            min_cap = max(min_cap , weights[i])
            max_cap += weights[i]

        result = self.doBinarySearchOnAnswer(min_cap , max_cap , weights , days) 
        return result

    def doBinarySearchOnAnswer(self , low : int , high : int , weights : list[int] , days : int) -> int : 
        ans = 0

        while low<=high : 
            mid = low + (high - low)//2 

            if self.calculateDays(mid , weights) <= days :
                ans = mid
                high = mid - 1

            else : 
                low = mid + 1

        return ans

    def calculateDays(self , n : int , weights : list[int]) -> int : 
        count = 0
        running_sum = 0

        for i in range(len(weights)) :
            if running_sum + weights[i] > n : 
                running_sum = 0
                count += 1
            running_sum += weights[i]
        
        return count+1