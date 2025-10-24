# Last updated: 10/24/2025, 8:36:22 PM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [0]*(len(edges)+1)
        self.rank = [1]*(len(edges)+1)

        for i in range(len(self.parent)) : 
            self.parent[i] = i

        for u , v in edges : 
            flag = self.findUnion(u , v)
            if flag == False :
                return [u,v]
        
        return []
    
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