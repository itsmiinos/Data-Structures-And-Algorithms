import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        my_heap = []
        for point in points :
            dist = (point[0] ** 2) + (point[1] ** 2)
            if len(my_heap) < k :
                heapq.heappush(my_heap , (-dist , [point[0] , point[1]]))
            else :
                heapq.heappush(my_heap , (-dist , [point[0] , point[1]]))
                heapq.heappop(my_heap)
        ans = []
        while len(my_heap) > 0 :
            ans.append(heapq.heappop(my_heap)[1])
        
        return ans
