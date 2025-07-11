import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = list(range(n)) # to keep track of the free rooms
        heapq.heapify(free_rooms)
        booking_freq = [0]*n
        busy_rooms = [] # to keep track of the next meeting end time
        meetings.sort()
        
        for start , end in meetings : 

            while len(busy_rooms) > 0 and busy_rooms[0][0] <= start : 
                end_time , room_id = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms , room_id)
            
            if len(free_rooms) > 0 :
                room_id = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms , (end , room_id))
                booking_freq[room_id] +=1
            
            else : 
                end_time , room_id = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms , (end_time + (end - start) , room_id))
                booking_freq[room_id] +=1

        
            
        max_used = 0
        for i in range(1 , len(booking_freq)) : 
            if booking_freq[max_used] < booking_freq[i] : 
                max_used = i

        return max_used


    

    def assignMeetingRoom(self , meeting_rooms , booking_freq) -> int : 

        for i in range(len(meeting_rooms)) : 
            if meeting_rooms[i] == False : 
                meeting_rooms[i] = True
                booking_freq[i] +=1
                return i
        
        return -1 # incase no rooms are availaible
    
    def deAssignMeetingRoom(self , meeting_rooms , room_id) -> None : 

        meeting_rooms[room_id] = False

    
