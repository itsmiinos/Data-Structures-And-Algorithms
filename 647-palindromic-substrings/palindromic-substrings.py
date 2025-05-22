class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[-1 for j in range(len(s))] for i in range (len(s))]
        result = 0
        for i in range(len(s)) :
            result += self.countSubstringsHelper(s , i , i , dp) #odd length
            result += self.countSubstringsHelper(s , i , i + 1, dp) #even length
        return result

    def countSubstringsHelper(self , s:str , l:int , r:int , dp:List[List[int]]) -> int :
        if l<0 or r>=len(s) :
            return 0
        if dp[l][r] !=-1 : return dp[l][r]

        if s[l] == s[r] : 
            dp[l][r] = self.countSubstringsHelper(s , l-1 , r+1 , dp) + 1
        else : 
            dp[l][r] = 0
        
        return dp[l][r]
