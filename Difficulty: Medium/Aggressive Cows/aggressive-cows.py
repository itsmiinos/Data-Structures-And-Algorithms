class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        
        # your code here
        minimum_distance_between_cows = float('inf')
        maximum_distance_between_cows = stalls[-1] - stalls[0]
        
        for i in range(1, len(stalls)) : 
            distance = stalls[i] - stalls[i-1]
            minimum_distance_between_cows = min(minimum_distance_between_cows , distance)
            
        result = self.doBinarySearchOnAnswer(minimum_distance_between_cows , maximum_distance_between_cows , k , stalls)
        
        return result
    
    def doBinarySearchOnAnswer(self,  low : int , high : int , k : int , stalls : [int]) -> int :
        ans = 0
        while low<=high : 
            
            mid = low + ((high - low)//2)
            
            if self.checkCowsFittedInDistance(mid , stalls) < k : 
                high = mid - 1
            
            else : 
                ans = mid
                low = mid + 1
            
        
        return ans
    
    def checkCowsFittedInDistance(self , n : int , stalls : [int]) -> int : 
        last_stalled = 0
        count = 1
        
        for i in range(len(stalls)) : 
            if stalls[i] - stalls[last_stalled] >= n : 
                count+=1
                last_stalled = i
            
        
        return count
