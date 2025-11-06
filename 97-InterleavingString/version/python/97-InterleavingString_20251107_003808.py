# Last updated: 11/7/2025, 12:38:08 AM
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        return self.solve(s1 , s2 , s3 , 0 , 0 , 0 , dp)
    
    def solve(self , s1 : str , s2 : str , s3 : str , i : int , j : int , k : int , dp : tuple) -> bool:

        if i >= len(s1) and j >= len(s2) and k >= len(s3) : 
            return True
        elif k >= len(s3) : 
            return False
        
        if (i , j , k) in dp : 
            return dp[(i, j , k)]
        

        
        if i < len(s1) and j < len(s2) and s3[k] == s1[i] and s3[k] == s2[j] : 
            dp[(i , j , k)] = self.solve(s1 , s2 , s3 , i+1 , j , k + 1 , dp) or self.solve(s1 , s2 , s3 , i , j+1 , k + 1 , dp)
            return dp[(i , j , k)]
        elif j < len(s2) and s3[k] == s2[j] :
            dp[(i , j , k)] = self.solve(s1 , s2 , s3 , i , j+1 , k + 1 , dp)
            return dp[(i , j , k)]
        elif i < len(s1) and s3[k] == s1[i] :
            dp[(i , j , k)] = self.solve(s1 , s2 , s3 , i+1 , j , k + 1 , dp)
            return dp[(i , j , k)]