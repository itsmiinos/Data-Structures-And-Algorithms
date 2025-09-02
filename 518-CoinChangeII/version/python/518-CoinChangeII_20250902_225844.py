# Last updated: 9/2/2025, 10:58:44 PM
class Solution:
    def change(self, sum: int, coins: List[int]) -> int:
              
        dp = [[-1 for i in range(sum+1)] for i in range(len(coins))]
        result = self.doDFS(coins , len(coins)-1 , sum , dp)
        return result
        
    
    def doDFS(self , coins : list[int] , n : int , sum : int , dp : list[list[int]]) -> int : 
        if sum == 0 : 
            return 1
        
        if sum!=0 and n < 0 : 
            return 0
        
        if dp[n][sum]!= -1 : 
            return dp[n][sum]
        
        if coins[n] <= sum : 
            taken = self.doDFS(coins , n , sum - coins[n] , dp)
            not_taken = self.doDFS(coins , n-1 , sum  , dp)
            
            dp[n][sum] = taken + not_taken
            
            return dp[n][sum]
        
        else : 
            
            dp[n][sum] = self.doDFS(coins , n-1 , sum , dp)
            return dp[n][sum]