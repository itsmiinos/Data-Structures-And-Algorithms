import heapq

class Solution:
   def minCost(self, arr):
    # code here
    heap = []
    connections = []
    
    for i in range(len(arr)) : 
        heapq.heappush(heap , arr[i])
    
    while len(heap) > 1 : 
        popped1 = heapq.heappop(heap)
        popped2 = heapq.heappop(heap)
        
        connect_cost = popped1 + popped2
        heapq.heappush(heap , connect_cost)
        connections.append(connect_cost)
    
    sum = 0
    for c in connections : 
        sum+=c
    
    return sum
        