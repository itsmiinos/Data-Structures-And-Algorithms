# Last updated: 9/16/2025, 2:09:30 AM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0

        for i in range(len(nums)) : 
            total_sum = total_sum + nums[i]
    
        if total_sum % 2 == 0 : 
            dp = [[False for j in range((total_sum // 2)+1)] for i in range(len(nums))] 
            # return self.doDFS(nums , len(nums)-1 , total_sum // 2 , dp)

            for i in range(len(dp)) : 
                for j in range(len(dp[0])) : 
                    if j == 0 : 
                        dp[i][j] = True # answer is always true for SUM = 0
            
            if nums[0] == total_sum // 2 : 
                dp[0][nums[0]] = True # This is done so that if there is an element which is less than sum and thats the only element then we make the answer True , instead of writing the index of the column we took the element as the index

            for i in range(len(dp)) : 
                for j in range(len(dp[0])) : 
                    if nums[i] <= j : # if the element is smaller than the sum
                        a = dp[i-1][j-nums[i]]
                        b = dp[i-1][j]
                        dp[i][j] = a or b
                    else : 
                        dp[i][j] = dp[i-1][j]
            
            return dp[len(nums)-1][total_sum//2]
        
        else : 
            return False

    # def doDFS(self , arr : list[int] , n : int , sum : int , dp : list[list]) -> bool : 
    #     if sum == 0 : 
    #         return True
        
    #     if n == -1 and sum!= 0 : 
    #         return False
        
    #     if dp[n][sum] != None : 
    #         return dp[n][sum]
        
    #     if arr[n] <= sum : 
    #         a = self.doDFS(arr , n-1 , sum - arr[n] , dp)
    #         b = self.doDFS(arr , n-1 , sum , dp)
    #         dp[n][sum] = a or b
    #         return a or b
        
    #     else : 
    #         dp[n][sum] =  self.doDFS(arr , n-1 , sum , dp)
    #         return dp[n][sum]