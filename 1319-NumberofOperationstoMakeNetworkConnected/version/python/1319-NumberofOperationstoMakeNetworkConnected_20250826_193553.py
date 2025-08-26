# Last updated: 8/26/2025, 7:35:53 PM
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.parent = [None]*n
        self.rank = [1]*n

        if len(connections) < n - 1 : 
            return -1

        for i in range(len(self.parent)) :
            self.parent[i] = i

        
        for u ,v in connections: 
            self.findUnion(u,v)
                
        
        count_components = 0
        for i in range(len(self.parent)) : 
            if self.parent[i] == i : 
                count_components +=1
        
        
        return count_components - 1
    
    def findUnion(self , u : int , v : int) -> bool : 
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)

        if parent_u == parent_v : 
            return False
        
        else : 
            if self.rank[parent_u] > self.rank[parent_v] : 
                self.parent[parent_v] = parent_u
            elif self.rank[parent_v] > self.rank[parent_u] :
                self.parent[parent_u] = parent_v
            else : 
                self.parent[parent_u] = parent_v
                self.rank[parent_v] +=1

        return True
    
    def findParent(self , x : int) -> int :
        if self.parent[x] == x : 
            return x
        
        temp = self.findParent(self.parent[x])
        self.parent[x] = temp
        return temp