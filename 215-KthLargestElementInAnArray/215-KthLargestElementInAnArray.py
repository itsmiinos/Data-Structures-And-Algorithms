# Last updated: 8/13/2025, 8:21:11 PM
import heapq
class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        heap = []
        
        for i in range(len(arr)) :
            if len(heap) < k : 
                heapq.heappush(heap , arr[i])
            else : 
                if arr[i] > heap[0] :
                    heapq.heappop(heap)
                    heapq.heappush(heap , arr[i])
        return heapq.heappop(heap)