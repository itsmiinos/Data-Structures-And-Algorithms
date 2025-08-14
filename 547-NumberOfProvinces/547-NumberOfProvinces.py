# Last updated: 8/15/2025, 12:13:44 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.ans = [0]*len(isConnected[0])
        self.rank = [0]*len(self.ans) # union by rank

        for i in range(len(self.ans)) : 
            self.ans[i] = i
        
        edges = self.makeEdges(isConnected)

        for u , v in edges : 
            self.findUnion(u , v)

        count = 0

        for i in range(len(self.ans)) : 
            if self.ans[i] == i : 
                count+=1
                
        return count
    
    def findUnion(self , u : int , y : int) -> None : 
        Pu = self.findParent(u)
        Py = self.findParent(y)

        if Pu == Py : return

        elif self.rank[Pu] == self.rank[Py] : # union by rank
            self.ans[Pu] = Py # union by rank
            self.rank[Py] +=1 # union by rank
        
        elif self.rank[Pu] > self.rank[Py] : # union by rank
            self.ans[Py] = Pu # union by rank

        elif self.rank[Py] > self.rank[Pu] : # union by rank
            self.ans[Pu] = Pu # union by rank


    def findParent(self , x : int) -> int : 

        if self.ans[x] == x : return x
        temp = self.findParent(self.ans[x])
        self.ans[x] = temp # path compression
        return temp
    

    def makeEdges(self , isConnected : list[list[int]]) -> list[list[int]] : 

        edges = []
        
        for i in range(len(isConnected)) : 
            for j in range(len(isConnected[i])) : 
                if isConnected[i][j] == 1 : 
                    edges.append([i , j])
        
        return edges