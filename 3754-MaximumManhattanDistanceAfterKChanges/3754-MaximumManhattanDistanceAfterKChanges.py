# Last updated: 8/13/2025, 8:14:55 PM
import sys
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        east  = 0 
        west = 0 
        north = 0 
        south = 0
        maxMD = -sys.maxsize
        for i in range(len(s)) : 
            if s[i] == 'N' : north+=1
            if s[i] == 'S' : south+=1
            if s[i] == 'E' : east +=1
            if s[i] == 'W' : west +=1

            currentMD = abs(east - west) + abs(north - south)
            wastedSteps = (i+1) - currentMD
            extra_needed = 0
            if wastedSteps > 0 : 
                extra_needed = min(2*k , wastedSteps)
            
            finalMD = currentMD + extra_needed

            maxMD = max(maxMD , finalMD)
        
        return maxMD
            
