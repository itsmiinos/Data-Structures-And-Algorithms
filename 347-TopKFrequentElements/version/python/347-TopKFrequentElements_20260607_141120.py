# Last updated: 6/7/2026, 2:11:20 PM
1import heapq
2class Solution:
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4        heap = []
5        freq = collections.defaultdict(int)
6
7        for i in range(len(nums)) :
8            freq[nums[i]] +=1
9
10        for key in freq.keys() :
11            val = freq[key]
12            if len(heap) < k : 
13                heapq.heappush(heap , [val , key])
14            elif val > heap[0][0] :
15                heapq.heappop(heap)
16                heapq.heappush(heap , [val , key])
17            
18            print(heap)
19        ans = []
20        while len(heap) > 0 :
21            ans.append(heapq.heappop(heap)[1])
22        
23        return ans
24        
25