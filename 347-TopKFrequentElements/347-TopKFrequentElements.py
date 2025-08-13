# Last updated: 8/13/2025, 8:20:01 PM
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        heap = []
        for i in range(len(nums)) :
            my_map[nums[i]] = my_map.get(nums[i] , 0) + 1
        
        for key in my_map : 
            if len(heap) < k : 
                heapq.heappush(heap , (my_map[key] , key))
            else : 
                if my_map[key] > heap[0][0] : 
                    heapq.heappop(heap)
                    heapq.heappush(heap , (my_map[key] , key))
        result = []
        while len(heap) > 0 : 
            result.append(heapq.heappop(heap)[1])
        
        return result
