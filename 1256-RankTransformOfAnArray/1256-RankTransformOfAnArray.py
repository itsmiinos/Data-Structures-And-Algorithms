# Last updated: 8/13/2025, 8:17:43 PM
import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = []
        rank = 1

        for i in range(len(arr)) : 
            heapq.heappush(heap , (arr[i] , i))
        
        while len(heap) > 0 : 
            element , index = heapq.heappop(heap)
            arr[index] = rank
            if heap and heap[0][0] > element : 
                rank+=1
        
        return arr