# Last updated: 11/9/2025, 9:58:23 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        i = 0
        j = len(people)-1

        while i <= j : 
            if i == j : 
                count+=1
                i+=1
                j-=1
            else :
                sum_of_weight = people[i] + people[j]
                if sum_of_weight > limit : 
                    count+=1
                    j-=1
                else : 
                    count+=1
                    i+=1
                    j-=1
        
        return count