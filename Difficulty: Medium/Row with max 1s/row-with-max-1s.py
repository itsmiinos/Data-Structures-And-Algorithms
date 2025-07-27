class Solution:
    
    def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        m = len(arr[0])
        max_index = 0
        max_zeros = 0
        
        for i in range(n) : 
            zero_count = self.calculateZeros(arr[i])
            if  zero_count > max_zeros : 
                max_zeros = zero_count
                max_index = i
            
        return max_index
    
    
    def calculateZeros(self , arr) : 
        
        low = 0
        high = len(arr) - 1
        
        ans = len(arr)
        
        while low <= high :
            
            mid = low + (high - low) // 2
            
            if arr[mid] == 1 : 
                ans = mid
                high = mid - 1
                
            
            else : 
                low = mid + 1
        
        
        return len(arr) - ans
        