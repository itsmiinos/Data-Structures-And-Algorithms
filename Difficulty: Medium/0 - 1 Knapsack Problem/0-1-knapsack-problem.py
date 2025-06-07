class Solution:
    def knapsack(self, W, val, wt):
        # code here
        dp = [[-1 for j in range (W+1)] for i in range (len(val))]
        result = self.knapsackHelper(W , val , wt , len(val)-1 , dp)
        return result
        
    def knapsackHelper(self , W : int , val : [int] , wt : [int] , i : int , dp : list[list[int]]) -> int : 
        
        if i<0 : 
            return 0
        if dp[i][W] !=-1 : return dp[i][W]
        
        temp1 = self.knapsackHelper(W , val , wt , i-1 , dp) #exclude
        temp2 = -1
        if wt[i] <= W : 
            temp2 = self.knapsackHelper(W-wt[i] , val , wt , i-1 , dp) + val[i] #include
            
        dp[i][W] = max(temp1 , temp2)
        
        return max(temp1 , temp2)
