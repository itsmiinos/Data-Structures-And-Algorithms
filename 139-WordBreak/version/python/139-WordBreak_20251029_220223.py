# Last updated: 10/29/2025, 10:02:23 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None]*(n+1)
        return self.solve(0 , s , wordDict , n , dp)

    def solve(self , i : int , s : str , wordDict : list[str] , n : int , dp : list[bool]) -> bool :

        if i == n : 
            return True
        
        if dp[i] is not None : 
            return dp[i] 

        for j in range(i+1 , n+1) : 
            split = s[i : j]

            if split in wordDict and self.solve(j , s , wordDict , n , dp) : 
                dp[i] = True
                return True
        dp[i] = False
        return False