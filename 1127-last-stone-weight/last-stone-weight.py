import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for i in range(len(stones)) :
            heapq.heappush(heap , -stones[i])
        
        while len(heap) > 1 :
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)
            diff = val1 - val2
            if diff > 0 :
                heapq.heappush(heap , -diff)
        
        if len(heap) > 0 :
            return -heap[0]
        
        return 0