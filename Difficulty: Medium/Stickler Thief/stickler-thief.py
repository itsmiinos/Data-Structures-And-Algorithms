class Solution:  
    def findMaxSum(self,arr):
        # code here
        dp = [-1]*len(arr)
        result = self.maxSumHelper(arr , len(arr)-1 , dp)
        return result
    
    def maxSumHelper(self , arr : [int] , i : int , dp : [int]) -> int :
        
        if(i<0) :
            return 0
        if dp[i]!=-1 : 
            return dp[i]
        
        a = self.maxSumHelper(arr , i-1 , dp)
        b = self.maxSumHelper(arr , i-2 , dp) + arr[i]
        
        dp[i] = max(a , b)
        return max(a,b)


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends