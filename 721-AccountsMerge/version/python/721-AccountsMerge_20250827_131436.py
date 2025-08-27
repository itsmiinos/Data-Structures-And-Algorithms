# Last updated: 8/27/2025, 1:14:36 PM
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = {}
        self.parent = [None]*len(accounts)
        self.rank = [1]*len(accounts)

        for i in range(len(self.parent)) : 
            self.parent[i] = i

        for i in range(len(accounts)) : 
            for j in range(1 , len(accounts[i])) : 
                if accounts[i][j] in hashmap : 
                    p = hashmap[accounts[i][j]]
                    self.findUnion(i , p)
                else : 
                    hashmap[accounts[i][j]] = i

        group_emails = {}

        for email , idx in hashmap.items() : 
            root = self.findParent(idx)
            if root in group_emails : 
                group_emails[root].append(email)
            else : 
                group_emails[root] = []
                group_emails[root].append(email)

        result = []
        for root , emails in group_emails.items() : 
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
                self.rank[parent_v] +=1
        
    def findParent(self , x : int) -> int :
        if self.parent[x] == x : 
            return x
        
        temp = self.findParent(self.parent[x])
        self.parent[x] = temp
        return temp
    