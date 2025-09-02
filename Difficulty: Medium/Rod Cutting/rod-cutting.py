#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        # n = len(price)
        # dp = [[0 for j in range(n+1)] for i in range(n+1)]
        
        # for i in range(1 , len(dp)) : 
        #     for j in range(len(dp[i])) :
        #         cutting_length = i
        #         cutting_price = price[i-1]
        #         if cutting_length <= j :
        #             dp[i][j] = max(dp[cutting_length-1][j] , dp[i][j-(cutting_length)] + cutting_price)
        #         else : 
        #             dp[i][j] = dp[cutting_length-1][j]
        
        # # result = self.doDFS(price , n-1 , n , dp)
        # return dp[n][n]
        
        n = len(price)
        
        # 1D DP: dp[i] = maximum profit for rod of length i
        dp = [0] * (n + 1)
        
        # For each length from 1 to n
        for length in range(1, n + 1):
            # Try all possible first cuts
            for cut in range(1, length + 1):
                # cut-1 because price array is 0-indexed
                dp[length] = max(dp[length], price[cut-1] + dp[length-cut])
        
        return dp[n]
    
    
    # def doDFS(self , price : list[int] , n : int , l:int , dp) -> int :
    #     if l == 0 :
    #         return 0
        
    #     if n < 0 : 
    #         return 0
            
    #     if dp[n][l]!= -1 : 
    #         return dp[n][l]
        
    #     if n+1 <= l : 
    #         divide = self.doDFS(price , n , l - (n+1) , dp) + price[n]
    #         not_divide = self.doDFS(price , n-1 , l , dp)
    #         dp[n][l] = max(divide , not_divide)
    #         return max(divide , not_divide)
    #     else : 
    #         dp[n][l] = self.doDFS(price , n-1 , l , dp)
    #         return dp[n][l]