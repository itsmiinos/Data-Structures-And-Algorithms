#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        dp = [[-1 for j in range (capacity+1)] for i in range (len(val))]
        result = self.knapsackHelper(val , wt , len(val)-1 , capacity , dp)
        return result
        
    def knapsackHelper(self , val : [int] , wt:[int] , i : int , W : int , dp : list[list[int]]) -> int : 
        
        if i < 0 : 
            return 0
            
        if dp[i][W] != -1 : return dp[i][W]
        
        temp1 = self.knapsackHelper(val , wt , i-1 , W , dp)
        temp2 = -1
        if wt[i] <=W : 
            temp2 = self.knapsackHelper(val , wt , i , W-wt[i] , dp) + val[i]
            
        dp[i][W] = max(temp1 , temp2)
        return dp[i][W]