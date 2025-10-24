# Last updated: 10/24/2025, 9:28:46 PM
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parent = [0]*(len(accounts)+1)
        self.rank = [1]*(len(accounts)+1)

        for i in range(len(self.parent)) : 
            self.parent[i] = i

        hashmap = {}

        for i in range(len(accounts)) :
            for j in range(1 , len(accounts[i])) : 
                if accounts[i][j] in hashmap : 
                    p = hashmap[accounts[i][j]]
                    self.findUnion(i , p)
                else : 
                    hashmap[accounts[i][j]] = i
        
        group_email = {}

        for email , idx in hashmap.items() : 
            parent = self.findParent(idx)
            if parent in group_email : 
                group_email[parent].add(email)
            else : 
                group_email[parent] = set()
                group_email[parent].add(email)
        
        result = []

        for root , emails in group_email.items() : 
            name = accounts[root][0]
            merged = [name] + sorted(emails)
            result.append(merged)
        
        return result

        

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
                self.rank[parent_v] = parent_u
        
        return
    
    def findParent(self , x : int) -> int : 
        if self.parent[x] == x : 
            return x
        
        temp = self.findParent(self.parent[x])
        self.parent[x] = temp

        return temp

