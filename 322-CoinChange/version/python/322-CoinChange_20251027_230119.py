# Last updated: 10/27/2025, 11:01:19 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        ans = self.doDP(len(coins) - 1, amount, coins, dp)
        return ans if ans != float('inf') else -1
    
    def doDP(self, i: int, amount: int, coins: List[int], dp: dict) -> int:

        if amount == 0:
            return 0
        if i < 0 or amount < 0:
            return float('inf')
        
        # Memoization check
        if (i, amount) in dp:
            return dp[(i, amount)]
        
        # Take coin[i] (don't move to i-1 since infinite supply)
        take = 1 + self.doDP(i, amount - coins[i], coins, dp)
        
        # Skip coin[i]
        not_take = self.doDP(i - 1, amount, coins, dp)
        
        dp[(i, amount)] = min(take, not_take)
        return dp[(i, amount)]