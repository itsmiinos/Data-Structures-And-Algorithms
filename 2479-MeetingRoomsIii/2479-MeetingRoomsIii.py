# Last updated: 8/13/2025, 8:16:01 PM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        busy_rooms = []
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        booking_freq = [0]*n
        max_freq_index = 0

        for start , end in meetings : 

            while len(busy_rooms) > 0 and busy_rooms[0][0] <= start : 
                popped_meeting = heapq.heappop(busy_rooms)
                free_room = popped_meeting[1]
                heapq.heappush(free_rooms , free_room)
            
            if len(free_rooms) > 0 : 
                popped_room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms , (end , popped_room))
                booking_freq[popped_room] +=1
            
            else : 
                popped_meeting = heapq.heappop(busy_rooms)
                new_end = end - start + popped_meeting[0]
                heapq.heappush(busy_rooms , (new_end , popped_meeting[1]))
                booking_freq[popped_meeting[1]] +=1
        
        for i in range(len(booking_freq)) : 
            if booking_freq[max_freq_index] < booking_freq[i] : 
                max_freq_index = i
            

        return max_freq_index
