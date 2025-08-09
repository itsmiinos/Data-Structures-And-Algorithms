from collections import deque

class Solution:
    def reverseFirstK(self, q, k):
        #code here 
        queue = deque()
        if k > len(q) : 
            return q
        for i in range(k-1 , -1 , - 1) : 
            queue.append(q[i])
        
        result = []
        n = len(queue)
        for i in range(n) : 
            result.append(queue.popleft())
        
        for i in range(k , len(q)) : 
            result.append(q[i])
        
        return result