# Last updated: 11/27/2025, 10:50:09 PM
1import heapq
2class MedianFinder:
3
4    def __init__(self):
5        self.max_heap = []
6        self.min_heap = []
7
8    def addNum(self, num: int) -> None:
9        if len(self.max_heap) == len(self.min_heap) : 
10            #first insert into min_heap then pop the min_heap to insert to max_heap
11            heapq.heappush(self.min_heap , num)
12            temp = heapq.heappop(self.min_heap)
13            heapq.heappush(self.max_heap , -temp)
14        else : 
15            #first we insert into max_heap then pop the max_heap to insert to min_heap
16            heapq.heappush(self.max_heap , -num)
17            temp = -heapq.heappop(self.max_heap)
18            heapq.heappush(self.min_heap , temp)
19
20    def findMedian(self) -> float:
21        if len(self.max_heap) > len(self.min_heap) : 
22            return -self.max_heap[0]
23        else : 
24            return (-self.max_heap[0] + self.min_heap[0]) / 2
25
26# Your MedianFinder object will be instantiated and called as such:
27# obj = MedianFinder()
28# obj.addNum(num)
29# param_2 = obj.findMedian()