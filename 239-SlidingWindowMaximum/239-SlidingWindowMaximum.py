# Last updated: 8/13/2025, 8:20:39 PM
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for i in range(k) : 
            while len(queue) >0 and queue[-1] < nums[i] : 
                queue.pop()
            
            queue.append(nums[i])
        
        result.append(queue[0])

        start = 0
        for i in range(k , len(nums)) : 
            while len(queue) >0 and queue[-1] < nums[i] : 
                queue.pop()
            
            queue.append(nums[i])

            if queue[0] == nums[i-k] : 
                queue.popleft()
            
            result.append(queue[0])
        
        return result
