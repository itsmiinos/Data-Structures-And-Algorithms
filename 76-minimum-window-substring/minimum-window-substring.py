class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""

        freq_t = collections.defaultdict(int)
        for i in range(len(t)) :
            freq_t[t[i]] +=1
        
        l = 0
        r = 0
        req_count = len(t)
        count = 0
        min_len = float('inf')
        min_start = -1

        while r < len(s) :
            if freq_t[s[r]] > 0 : # this mean we need that char
                count+=1
            
            freq_t[s[r]] -=1

            while count == req_count :
                if (r - l + 1) < min_len :
                    min_len = r - l + 1
                    min_start = l
                
                freq_t[s[l]]+=1

                if freq_t[s[l]] > 0 :
                    count-=1
                
                l+=1

            r+=1
        
        if min_start == -1 :
            return ""
        
        return s[min_start : min_start + min_len]
                
             
