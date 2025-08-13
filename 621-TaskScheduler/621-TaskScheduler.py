# Last updated: 8/13/2025, 8:19:20 PM
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()
        freq = [0]*26

        for task in tasks : 
            freq[ord(task) - ord('A')] += 1
        
        for i in range(len(freq)) : 
            if freq[i] > 0 : 
                heapq.heappush(heap , -freq[i])
        current_time = 0
        while len(heap) > 0 or len(queue) > 0: 
            if queue and current_time == queue[0].time: 
                heapq.heappush(heap , -queue.popleft().value)
            
            if len(heap) > 0 :
                popped = -heapq.heappop(heap)
                if popped - 1 != 0 : 
                    queue.append(Pair(popped - 1 , current_time + n + 1))
            
            current_time+=1
        
        return current_time



class Pair : 

    def __init__ (self , value : int, time : int) : 
        self.value = value
        self.time = time
