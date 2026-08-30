class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False

        s1_map = [0]*26
        s2_map = [0]*26

        for i in range(len(s1)) :
            s1_map[ord(s1[i]) - ord('a')] +=1
        
        i = 0 
        j = 0

        while (j - i + 1) < len(s1) :
            s2_map[ord(s2[j]) - ord('a')] +=1
            j+=1

        while j < len(s2) :

            s2_map[ord(s2[j]) - ord('a')] +=1

            if s1_map == s2_map :
                return True
            
            s2_map[ord(s2[i]) - ord('a')] -=1
            i+=1
            j+=1
        
        return False