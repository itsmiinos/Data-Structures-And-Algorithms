# Last updated: 8/13/2025, 8:20:18 PM
import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap) : 
            #first insert into min_heap then pop the min_heap to insert to max_heap
            heapq.heappush(self.min_heap , num)
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap , -temp)
        else : 
            #first we insert into max_heap then pop the max_heap to insert to min_heap
            heapq.heappush(self.max_heap , -num)
            temp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap , temp)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap) : 
            return -self.max_heap[0]
        else : 
            return (-self.max_heap[0] + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()