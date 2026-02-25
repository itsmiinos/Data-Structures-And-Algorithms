# Last updated: 2/25/2026, 2:05:33 PM
1import heapq
2class Solution:
3    def sortByBits(self, arr: List[int]) -> List[int]:
4        heap = []
5        for i in range(len(arr)) :
6            heapq.heappush(heap , (arr[i].bit_count() , arr[i]))
7        
8
9        ans = []
10        while len(heap) > 0 :
11            ans.append(heapq.heappop(heap)[1])
12        
13        return ans
14