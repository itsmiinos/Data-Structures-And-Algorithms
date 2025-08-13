# Last updated: 8/13/2025, 8:23:21 PM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[-1 for j in range(m)] for i in range(n)]
        result = self.minDistanceHelper(word1 , n-1 , word2 , m-1, dp)
        return result

    def minDistanceHelper(self , word1 : str , i : int , word2 : str , j : int , dp : List[List[int]]) -> int : 
        if i ==-1 and j==-1 : return 0
        if i==-1 and j!=-1 : return j+1 #return the left over to be added
        if i!=-1 and j==-1 : return i+1 #return the deletion to be done

        if dp[i][j]!= -1: return dp[i][j]

        if word1[i] == word2[j] :
            x = self.minDistanceHelper(word1 , i-1 , word2 , j-1 , dp)
            dp[i][j] = x
            return x
        else :
            x = self.minDistanceHelper(word1 , i-1 , word2 , j , dp) #delete word1
            y = self.minDistanceHelper(word1 , i-1 , word2 , j-1 , dp) #replace char in word1
            z = self.minDistanceHelper(word1 , i , word2 , j-1 , dp) #add to word1

            dp[i][j] = min(x,y,z) + 1
            return dp[i][j]