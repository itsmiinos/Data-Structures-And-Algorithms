# Last updated: 8/28/2025, 9:59:50 PM
import heapq
class Pair : 
    def __init__(self , value : int , cost : int , stops : int) -> None : 
        self.cost = cost
        self.stops = stops
        self.value = value
    def __lt__(self , other) :
        return self.cost < other.cost

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = self.createAdj(flights , n)
        heap = []

        heapq.heappush(heap , Pair(src , 0 , 0))
        
        best = {}
        while len(heap) > 0 : 
            rem = heapq.heappop(heap)
            value = rem.value
            cost = rem.cost
            stops = rem.stops

            if value == dst : 
                return cost


            if stops > k : 
                continue

            
        
            for nei, price in adj[value]:
                new_cost = cost + price
                if (nei, stops) not in best or new_cost < best[(nei, stops)]:
                    best[(nei, stops)] = new_cost
                    heapq.heappush(heap, Pair(nei, new_cost, stops + 1))

        
        return -1

    


    def createAdj(self , flights : list[list[int]] , n : int) -> list[list[int]] :
        adj = [[] for _ in range(n)]

        for u , v , w in flights : 
            adj[u].append([v , w])
        
        return adj