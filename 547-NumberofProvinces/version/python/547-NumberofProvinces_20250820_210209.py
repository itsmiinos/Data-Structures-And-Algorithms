# Last updated: 8/20/2025, 9:02:09 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.parent = [None]*len(isConnected)
        self.rank = [1]*len(isConnected)

        for i in range(len(isConnected)) : 
            self.parent[i] = i
        
        edges = self.createEdges(isConnected)

        for u,v in edges : 
            self.findUnion(u,v)
        count = 0
        for i in range (len(self.parent)) : 
            if self.parent[i] == i :
                count +=1
        
        return count
        

    
    def findUnion(self , u : int , v : int) -> None :

        parent_u = self.findParent(u)
        parent_v = self.findParent(v)

        if parent_u == parent_v : 
            return
        
        else : 
            if self.rank[parent_u] > self.rank[parent_v] :
                self.parent[parent_v] = parent_u
            
            elif self.rank[parent_v] > self.rank[parent_u] :
                self.parent[parent_u] = parent_v
            
            else : 
                self.parent[parent_u] = parent_v
                self.rank[parent_v] +=1
    

    def findParent(self , x : int) -> int :

        if self.parent[x] == x : 
            return x
        
        temp = self.findParent(self.parent[x])
        self.parent[x] = temp

        return temp
    

    def createEdges(self , isConnected : list[list[int]]) -> list[list[int]]: 

        edges = []

        for i in range(len(isConnected)) :
            for j in range(len(isConnected[i])) : 
                if isConnected[i][j] == 1 : 
                    edges.append([i , j])

        return edges 