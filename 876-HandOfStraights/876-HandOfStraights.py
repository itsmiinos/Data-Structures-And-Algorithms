# Last updated: 8/13/2025, 8:18:43 PM
import heapq
from collections import deque

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heap = []
        my_map = {}
        queue = deque()

        if len(hand)%groupSize != 0 : 
            return False

        for i in range(len(hand)) : 
            my_map[hand[i]] = my_map.get(hand[i] , 0) + 1
        
        for key in my_map : 
            heapq.heappush(heap , key)
        
        while heap : 
            first = heap[0]

            for i in range(groupSize) : 
                number = first + i

                if number not in my_map : 
                    return False
                
                my_map[number] = my_map.get(number) - 1
                if my_map[number] == 0 :
                    del my_map[number]
                    heapq.heappop(heap)
        
        
        return True