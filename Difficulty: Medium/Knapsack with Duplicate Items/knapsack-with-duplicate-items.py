#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        dp = [[-1 for j in range(capacity+1)] for i in range(len(val) + 1)]
        result = self.knapsackHelper(val , wt , capacity , len(val)-1 , dp)
        return result
        
    def knapsackHelper(self , val : [int] , wt : [int] , capacity : int , i:int , dp : list[list[int]]) -> int : 
        if i < 0 or capacity == 0 : 
            return 0
        
        if dp[i][capacity] != -1 : return dp[i][capacity]
        
        a = self.knapsackHelper(val , wt , capacity , i-1 , dp)
        b = -1 
        if wt[i] <= capacity :
            b = self.knapsackHelper(val , wt , capacity - wt[i] , i , dp) + val[i]
        
        dp[i][capacity] = max(a , b)
        return dp[i][capacity]