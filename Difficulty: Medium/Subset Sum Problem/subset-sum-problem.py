class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        # dp = [[-1 for j in range(sum+1)] for i in range(n)]    
        # result = self.doDFS(arr , n-1 , sum , dp)
        
        dp = [[None for j in range(sum + 1)] for i in range (n)]
        
        for i in range(len(dp)) : 
            for j in range(len(dp[i])) : 
                if j ==0 : 
                    dp[i][j] = True
        
        if arr[0] <= sum:
            dp[0][arr[0]] = True     
        
        for i in range(len(dp)) : 
            for j in range(len(dp[i])) : 
                if arr[i] <= j : 
                    a = dp[i-1][j-arr[i]]
                    b = dp[i-1][j]
                    dp[i][j] = a or b
                
                else : 
                    dp[i][j] = dp[i-1][j]
        
        return dp[n-1][sum]
                
        
        # return result
    
    # For bottom up approach
    # def doDFS(self , arr : list[int] , n : int , sum : int , dp : list[list]) -> bool : 
    #     if sum == 0 : 
    #         return True
        
    #     if n == -1 and sum!= 0 : 
    #         return False
        
    #     if dp[n][sum] != -1 : 
    #         return dp[n][sum]
        
    #     if arr[n] <= sum : 
    #         a = self.doDFS(arr , n-1 , sum - arr[n] , dp)
    #         b = self.doDFS(arr , n-1 , sum , dp)
    #         dp[n][sum] = a or b
    #         return a or b
        
    #     else : 
    #         dp[n][sum] =  self.doDFS(arr , n-1 , sum , dp)
    #         return dp[n][sum]
    
        
        
        