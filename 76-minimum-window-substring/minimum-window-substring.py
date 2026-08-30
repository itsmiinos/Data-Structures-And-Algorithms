class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""

        t_map = collections.defaultdict(int)
        
        for i in range(len(t)):
            t_map[t[i]] +=1

        i = 0
        j = 0
        min_start = -1
        min_len = float('inf')
        s_map = collections.defaultdict(int)

        while j < len(s) :
            s_map[s[j]] +=1

            while self.s_contains_t(s_map , t_map) :
                
                if (j - i + 1) < min_len :
                    min_start = i
                    min_len = (j - i + 1)
                
                s_map[s[i]]-=1
                i+=1
            
            j+=1
        
        if min_start == -1 :
            return ""
            
        return s[min_start : min_start + min_len]

    def s_contains_t(self , s_map , t_map) -> bool :

        for key in t_map.keys() :
            if key not in s_map or t_map[key] > s_map[key] :
                return False
        
        return True
        
            
