class Solution:
    def knapsack(self, W, val, wt):
        # code here
        dp = [[-1 for j in range(W+1)] for i in range(len(val))]
        result = self.knapsackHelper(W , val , wt , dp, len(val)-1)
        return result
        
    def knapsackHelper(self , K : int , val : [int] , wt : [int] , dp : list[list[int]] , i: int) -> int :
        if i<0 : return 0
        if dp[i][K] != -1 : return dp[i][K]
        a = self.knapsackHelper(K , val , wt , dp , i-1) #exclude
        b = -1
        if wt[i] <= K : 
            b = self.knapsackHelper(K - wt[i] , val , wt , dp , i-1) + val[i] # include
        dp[i][K] = max(a,b)
        return max(a,b)
        



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends