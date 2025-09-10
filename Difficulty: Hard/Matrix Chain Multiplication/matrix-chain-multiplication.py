class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        
        result = self.doDP(arr , 1 , len(arr)-1 , dp)
        return result
        
    
    def doDP(self , arr : list[int] , i : int , j : int , dp:list[list[int]]) -> int : 
        
        if i>= j : 
            return 0
            
        if dp[i][j] != -1 : 
            return dp[i][j]
        
        
        min_cost = float('inf')
        for k in range(i , j) :
            temp = self.doDP(arr , i , k , dp) + self.doDP(arr , k+1 , j , dp) + (arr[i-1] * arr[k] * arr[j])
            
            min_cost = min(min_cost , temp)
        dp[i][j] = min_cost
        return min_cost
        