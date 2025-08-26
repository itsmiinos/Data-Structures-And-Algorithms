# Last updated: 8/26/2025, 9:08:15 PM
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = max(r for r, c in stones)
        max_col = max(c for r, c in stones)
        
        n = max_row + max_col + 2  # total nodes (row nodes + col nodes)
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

        used = set()
        for r, c in stones:
            self.findUnion(r, c + max_row + 1)
            used.add(r)
            used.add(c + max_row + 1)

        # Count number of unique connected components among used nodes
        components = set()
        for u in used:
            components.add(self.findParent(u))

        return len(stones) - len(components)

    def findUnion(self, u: int, v: int) -> bool:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True

    def findParent(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])  # path compression
        return self.parent[x]
