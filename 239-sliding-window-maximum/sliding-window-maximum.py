from collections import deque
# import sys

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        # maximum_value = -sys.maxsize
        result = []
        for i in range(k) : 
            while len(q) > 0 and nums[i] > q[-1] : 
                q.pop()
            q.append(nums[i])
        
        result.append(q[0])

        for i in range(k , len(nums)) : 
            while len(q) > 0 and nums[i] > q[-1] : 
                q.pop()
            
            q.append(nums[i])

            if q[0] == nums[i-k] : 
                q.popleft()
            result.append(q[0])
        
        return result
