#User function Template for python3

class Solution:
    def minTime (self, arr, k):
        #code here
        max_value = -float('inf')
        sum_of_all_tasks = 0
        
        for i in range(len(arr)) : 
            max_value = max(max_value , arr[i])
            sum_of_all_tasks += arr[i]
        
        result = self.doBinarySearch(max_value , sum_of_all_tasks , k , arr)
        return result
    
    def doBinarySearch(self , low : int , high : int , k : int , arr : [int]) -> int : 
        
        ans = 0
        while low <= high : 
            mid = low + ((high - low) // 2)
            
            if self.checkWorkerCount(mid , arr) <= k : 
                ans = mid
                high = mid - 1
            
            else : 
                low = mid + 1
        
        return ans
    
    def checkWorkerCount(self , w: int , arr : [int]) -> int : 
        
        running_sum = 0
        count = 0
        i = 0
        
        while i < len(arr) : 
            if running_sum + arr[i] > w : 
                count+=1
                running_sum = 0
            
            running_sum += arr[i]
            i+=1
        
        return count+1
            
        