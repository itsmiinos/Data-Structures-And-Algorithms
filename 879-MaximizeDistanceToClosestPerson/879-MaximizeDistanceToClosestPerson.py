# Last updated: 8/13/2025, 8:18:42 PM
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        previous_occ = -1
        max_distance = 0

        for i in range(len(seats)) : 
            if seats[i] == 1 : 
                if previous_occ == -1 : 
                    max_distance = i

                else : 
                    max_distance = max(max_distance , (i-previous_occ)//2)

                previous_occ = i
        
        max_distance = max(max_distance , len(seats) - 1 - previous_occ)
        return max_distance