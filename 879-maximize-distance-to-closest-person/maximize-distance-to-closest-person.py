import sys
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last_one_index = -1
        max_dist = -sys.maxsize
        for i in range(len(seats)) : 
            if seats[i] == 1 :
                if last_one_index == -1 : 
                    max_dist = max(max_dist , i)
                else : 
                    max_dist = max(max_dist , (i - last_one_index )// 2)
                last_one_index = i 
        
        if seats[len(seats) - 1] == 0 :
            max_dist = max(max_dist , len(seats) - 1 - last_one_index)

        return max_dist

        