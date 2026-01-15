# Last updated: 1/16/2026, 2:16:51 AM
1import heapq
2from collections import defaultdict
3class Solution:
4    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
5        freq = defaultdict(int)
6        for i in range(len(nums)) :
7            freq[nums[i]] +=1
8
9        heap = []
10        for key in freq.keys() :
11            heapq.heappush(heap , (-freq[key] , key))
12        
13        ans = []
14        while k > 0 :
15            f , v  = heapq.heappop(heap)
16            ans.append(v)
17            k-=1
18        
19        return ans