# Last updated: 8/15/2025, 12:12:06 AM
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.parent_alice = [0]*(n+1)
        self.parent_bob = [0]*(n+1)

        self.rank_alice = [0]*(n+1)
        self.rank_bob = [0]*(n+1)

        for i in range(n+1) : 
            self.parent_alice[i] = i
            self.parent_bob[i] = i

        edges = sorted(edges , key = lambda x : -x[0] )

        count = 0
        count_alice = 0
        count_bob = 0

        for t , u , v in edges : 
            if t == 3 : 
                merge_alice = self.findUnion(u , v , self.parent_alice , self.rank_alice)
                merge_bob = self.findUnion(u , v , self.parent_bob , self.rank_bob)
                if merge_alice == False and merge_bob == False : 
                    count+=1
                else : 
                    if merge_alice == True : count_alice+=1
                    if merge_bob == True : count_bob+=1


            elif t == 2 : 
                merge_bob = self.findUnion(u , v , self.parent_bob ,self.rank_bob)
                if merge_bob == False : 
                    count+=1
                else : 
                    count_bob+=1
            else : 
                merge_alice = self.findUnion(u , v , self.parent_alice , self.rank_alice)
                if merge_alice == False: 
                    count+=1
                else : 
                    count_alice+=1
        
        if count_alice == n-1 and count_bob == n-1 : 
            return count
        else : 
            return -1

        
        

    
    def findUnion(self , u : int , v : int , parent : list[int] , rank : list[int]) -> bool :
        merge = False

        Pu = self.findParent(u , parent)
        Pv = self.findParent(v , parent)

        if Pu == Pv : return False

        elif rank[Pu] > rank[Pv] : 
            parent[Pv] = Pu
        
        elif rank[Pv] > rank[Pu] : 
            parent[Pu] = Pv

        else : 
            parent[Pu] = Pv
            rank[Pv] +=1

        return True

   
    def findParent(self , x : int , parent : list[int]) -> int : 
        
        if parent[x] == x : 
            return x

        temp = self.findParent(parent[x] , parent)
        parent[x] = temp
        return temp
     