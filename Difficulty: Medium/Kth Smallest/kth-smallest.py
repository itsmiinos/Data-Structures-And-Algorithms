#User function Template for python3

import heapq
class Solution:

    def kthSmallest(self, arr,k):
        my_heap = []
        
        for i in range (k) : 
            heapq.heappush(my_heap , -arr[i])
        
        for i in range(k , len(arr)) : 
            if arr[i] < -my_heap[0] : 
                heapq.heappop(my_heap)
                heapq.heappush(my_heap , -arr[i])
        
        return -heapq.heappop(my_heap)
        
