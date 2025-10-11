# Last updated: 10/11/2025, 11:09:43 PM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)

        if not trust and n == 1 : # where in the town there is only a town judge 
            return 1
    
        for u , v in trust : 
            indegree[v] +=1
            outdegree[u] +=1
        
        for i in range(n+1) : 
            if indegree[i] == n-1 and outdegree[i] == 0 :
                return i
        
        return -1
        
        