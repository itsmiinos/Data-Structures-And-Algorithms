#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        n = len(val)
        dp = [[-1 for j in range(capacity+1)] for i in range(n)]
        result = self.knapSackHelper(val , wt , capacity , n-1 , dp)
        return result
        
    def knapSackHelper(self , val : [int] , wt: [int] , capacity:int ,  i:[int] , dp : list[list[int]]) -> int :
        if i < 0 :
            return 0
        if dp[i][capacity] != -1 : return dp[i][capacity]
        a = self.knapSackHelper(val , wt , capacity , i-1 , dp) #exclude
        b = -1
        if wt[i] <= capacity :
            b = self.knapSackHelper(val , wt , capacity - wt[i] , i , dp) + val[i]
            
        res = max(a,b)
        dp[i][capacity] = res
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends