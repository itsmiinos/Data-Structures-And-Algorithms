
from typing import List


class Solution:
    def countPartitions(self, arr, d):
        # code here
        total_sum = 0
        
        for i in range(len(arr)) : 
            total_sum += arr[i]
            
        if (total_sum - d) % 2 != 0 or total_sum < d: 
            return 0
        
        s = (total_sum - d) // 2
        dp = [[-1 for j in range(s+1)] for i in range(len(arr))]    
        
        return self.doDFS(arr , len(arr)-1 , s , dp)
        
    
    def doDFS(self , arr : list[int] , n : int , sum : int , dp : list[list]) -> int : 
        if n == 0:
            if sum == 0 and arr[0] == 0:
                return 2
            if sum == 0 or sum == arr[0]:
                return 1
            return 0
        
        if dp[n][sum] != -1 : 
            return dp[n][sum]
        
        if arr[n] <= sum : 
            a = self.doDFS(arr , n-1 , sum - arr[n] , dp)
            b = self.doDFS(arr , n-1 , sum , dp)
            dp[n][sum] = a + b
            return a + b
        
        else : 
            dp[n][sum] =  self.doDFS(arr , n-1 , sum , dp)
            return dp[n][sum]
        
