import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = []

        for i in range (k) : 
            heapq.heappush(my_heap, nums[i])
        
        for i in range ( k , len(nums)) : 
            if nums[i] > my_heap[0] : 
                heapq.heappop(my_heap)
                heapq.heappush(my_heap , nums[i])
        
        return my_heap[0]