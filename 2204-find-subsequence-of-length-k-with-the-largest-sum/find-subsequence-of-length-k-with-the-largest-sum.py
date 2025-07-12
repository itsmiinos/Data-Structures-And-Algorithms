class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(len(nums)) : 
            if len(heap) < k : 
                heapq.heappush(heap , (nums[i] , i))
            
            else : 
                if nums[i] > heap[0][0] : 
                    heapq.heappop(heap)
                    heapq.heappush(heap , (nums[i] , i))

        heap.sort(key=lambda x : x[1])
        result = []
        
        for u in heap : 
            result.append(u[0])
        
        return result