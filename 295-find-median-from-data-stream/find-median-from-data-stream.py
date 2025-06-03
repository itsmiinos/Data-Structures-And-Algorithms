import heapq
class MedianFinder:

    def __init__(self):
        self.my_min_heap = []
        self.my_max_heap = []
        self.data_count = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.my_max_heap, -num)

        # balance by pushing the largest from small to large
        heapq.heappush(self.my_min_heap, -heapq.heappop(self.my_max_heap))

        # maintain size property: len(small) >= len(large)
        if len(self.my_max_heap) < len(self.my_min_heap):
            heapq.heappush(self.my_max_heap, -heapq.heappop(self.my_min_heap))
        self.data_count+=1

    def findMedian(self) -> float:
        if self.data_count % 2 == 0 : 
            left_maximum = -self.my_max_heap[0]
            right_minimum = self.my_min_heap[0]
            median = float((left_maximum + right_minimum) / 2.0)
            return median
        else : 
            return float(-self.my_max_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()