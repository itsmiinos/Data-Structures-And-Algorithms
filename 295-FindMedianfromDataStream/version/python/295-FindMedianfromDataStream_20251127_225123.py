# Last updated: 11/27/2025, 10:51:23 PM
1import heapq
2class MedianFinder:
3
4    def __init__(self):
5        self.min_heap = []
6        self.max_heap = []
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
20
21    def findMedian(self) -> float:
22        if len(self.max_heap) > len(self.min_heap): 
23            return -(self.max_heap[0])
24        else : 
25            return (-self.max_heap[0] + self.min_heap[0]) / 2
26
27
28# Your MedianFinder object will be instantiated and called as such:
29# obj = MedianFinder()
30# obj.addNum(num)
31# param_2 = obj.findMedian()