# Last updated: 9/3/2025, 9:58:57 PM
class Solution:
    def coinChange(self, coins: List[int], sum: int) -> int:
        dp = [[-1 for i in range(sum+1)] for i in range(len(coins))]
        result = self.doDFS(coins , len(coins)-1 , sum , dp)
        if result != float('inf'):
            return result 
        else :
            return -1
        
    
    def doDFS(self , coins : list[int] , n : int , sum : int , dp : list[list[int]]) -> int : 
        if sum == 0 : 
            return 0
        
        if sum!=0 and n < 0 : 
            return float('inf')
        
        if dp[n][sum]!= -1 : 
            return dp[n][sum]
        
        if coins[n] <= sum : 
            taken = self.doDFS(coins , n , sum - coins[n] , dp) + 1
            not_taken = self.doDFS(coins , n-1 , sum  , dp)
            
            dp[n][sum] = min(taken , not_taken)
            
            return dp[n][sum]
        
        else : 
            
            dp[n][sum] = self.doDFS(coins , n-1 , sum , dp)
            return dp[n][sum]