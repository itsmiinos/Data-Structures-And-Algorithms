# Last updated: 1/27/2026, 8:11:34 PM
1import heapq
2class Solution:
3    def minCost(self, n: int, edges: List[List[int]]) -> int:
4        result = [float('inf')] * n
5        result[0] = 0
6        heap = []
7        heapq.heappush(heap , (0 , 0))
8        graph = self.createGraph(n , edges)
9        visited = [False] * n
10        visited[0] = True
11
12        while len(heap) > 0 :
13
14            dist , res = heapq.heappop(heap)
15            nei = graph[res]
16
17            for n , w in nei :
18                if (dist + w) < result[n] :
19                    result[n] = dist + w
20                    heapq.heappush(heap , (dist + w , n))
21                    visited[n] = True
22        
23        return result[-1] if visited[-1] == True else -1
24    
25
26    def createGraph(self , n : int , edges : list) -> list :
27
28        graph = []
29
30        for _ in range(n) :
31            graph.append([])
32        
33        for u , v , w in edges :
34            graph[u].append([v , w])
35            graph[v].append([u , 2*w])
36        
37        return graph
38        