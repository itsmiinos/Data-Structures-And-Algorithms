class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        max_weight = -float('inf')
        sum_of_all_weights = 0

        for i in range(len(weights)) : 
            max_weight = max(max_weight , weights[i])
            sum_of_all_weights += weights[i]
        
        # we got the high = sum_of_weights which will require 1 day and we got the low = max_weight which will require approx lenght of array if all the array is equal in the worst case

        result = self.doBinarySearch(max_weight , sum_of_all_weights , days , weights)
        return result
    
    def doBinarySearch(self , low : int , high : int , days : int , weights : [int]) -> int : 
        ans = 0
        while low<=high : 
            
            mid = low + ((high - low) // 2)
            
            if self.checkDays(mid ,weights) <= days : 
                ans = mid
                high = mid - 1
            
            else : 
                low = mid + 1
        
        return ans
    
    def checkDays(self , w : int , weights : [int]) -> int : 
        
        i = 0 
        running_sum = 0
        count = 0
        while i < len(weights) : 
            
            if running_sum + weights[i] > w : 
                count+=1
                running_sum = 0
            
            running_sum += weights[i]
            i+=1

        return count + 1
            

        
        

        