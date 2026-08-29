class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False
        
        s1_map = collections.defaultdict(int)
        for i in range(len(s1)) :
            s1_map[s1[i]] +=1
        
        i = 0
        j = 0

        s2_map = collections.defaultdict(int)

        while j < len(s2) :
            while j - i + 1 < len(s1) :
                s2_map[s2[j]] +=1
                j+=1

            s2_map[s2[j]] +=1

            if s2_map == s1_map :
                return True

            # print(s2_map , s1_map)
            s2_map[s2[i]]-=1
            if s2_map[s2[i]] == 0 :
                del s2_map[s2[i]]
            i+=1
            j+=1
        
        return False