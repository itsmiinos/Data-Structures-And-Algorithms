# Last updated: 8/13/2025, 8:19:44 PM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map_p = {}
        map_s = {}
        result = []

        if len(s) < len(p):
            return []

        for i in range(len(p)) : 
            map_p[p[i]] = map_p.get(p[i] , 0) + 1
        
        for i in range(len(p)) : 
            map_s[s[i]] = map_s.get(s[i] , 0) + 1
        
        if map_s == map_p : 
            result.append(0)
        
        for i in range(len(p) , len(s)) : 
            new_char = s[i]
            old_char = s[i-len(p)]

            map_s[new_char] = map_s.get(new_char , 0) + 1
            map_s[old_char] = map_s.get(old_char , 0) - 1

            if map_s[old_char] == 0 : 
                del map_s[old_char] 
            
            if map_s == map_p : 
                result.append(i-len(p) + 1)
        
        
        return result 