class Solution:
    def distinctSubseqII(self, s: str) -> int:
        self.prev = [None]*len(s)
        last_seen = [None]*26
        dp = [-1] * 2001
        self.MOD = (10 ** 9) + 7

        for i in range(len(s)) :
            index = ord(s[i]) - ord('a')
            if last_seen[index] is None :
                last_seen[index] = i
            else :
                self.prev[i] = last_seen[index]
                last_seen[index] = i
        
        return (self.solve(len(s)-1, dp) - 1) % self.MOD
    
    def solve(self, n:int , dp : list) -> int:
        if n == -1 :
            return 1
        if n == 0 :
            return 2
        if dp[n] != -1 :
            return dp[n]
        total = self.solve(n-1 , dp) * 2
        duplicates = 0
        if self.prev[n] is not None:
            duplicates = self.solve(self.prev[n] - 1 , dp)
        
        total -= duplicates
        dp[n] = (total + self.MOD) % self.MOD
        return (total + self.MOD) % self.MOD