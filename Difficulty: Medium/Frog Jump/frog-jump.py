#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        dp = [-1]*(len(height))
        return self.helper(height, len(height)-1, dp)
        return result

    def helper(self , height : list[int] , i : int , dp : [int]) : 
        if i == 0 :
            return 0
        if dp[i] !=-1 : return dp[i]

        temp1 = self.helper(height , i-1 , dp) + abs(height[i] - height[i-1])
        temp2 = float('inf')
        if i > 1:
            temp2 = self.helper(height, i-2, dp) + abs(height[i] - height[i-2])
        dp[i] = min(temp1 , temp2)
        return dp[i]