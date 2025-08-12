class Solution:
    def bellmanFord(self, V, edges, src):
        INF = 10**8  # or 100000000 as per problem statement
        ans = [INF] * V
        ans[src] = 0
        
        for _ in range(V - 1):
            for u, v, w in edges:
                if ans[u] != INF and ans[u] + w < ans[v]:
                    ans[v] = ans[u] + w
        
        # Optional negative cycle detection (if needed)
        haveNegativeCycle = False
        for u, v, w in edges:
                if ans[u] != INF and ans[u] + w < ans[v]:
                    return [-1]
        
        return ans
