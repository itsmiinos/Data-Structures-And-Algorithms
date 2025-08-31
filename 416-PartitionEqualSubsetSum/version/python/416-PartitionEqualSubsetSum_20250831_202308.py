# Last updated: 8/31/2025, 8:23:08 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0

        for i in range(len(nums)) : 
            total_sum = total_sum + nums[i]
        
        
        if total_sum % 2 == 0 : 
            dp = [[None for j in range((total_sum // 2)+1)] for i in range(len(nums))] 
            return self.doDFS(nums , len(nums)-1 , total_sum // 2 , dp)
        
        else : 
            return False

    def doDFS(self , arr : list[int] , n : int , sum : int , dp : list[list]) -> bool : 
        if sum == 0 : 
            return True
        
        if n == -1 and sum!= 0 : 
            return False
        
        if dp[n][sum] != None : 
            return dp[n][sum]
        
        if arr[n] <= sum : 
            a = self.doDFS(arr , n-1 , sum - arr[n] , dp)
            b = self.doDFS(arr , n-1 , sum , dp)
            dp[n][sum] = a or b
            return a or b
        
        else : 
            dp[n][sum] =  self.doDFS(arr , n-1 , sum , dp)
            return dp[n][sum]