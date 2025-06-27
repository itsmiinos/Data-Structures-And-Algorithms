import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_t = {}
        map_s = {}

        for i in range(len(t)) : 
            map_t[t[i]] = map_t.get(t[i] , 0) + 1
        
        start = 0
        ans_string = ""
        minimum_window_length = sys.maxsize
        for i in range(len(s)) : 
            map_s[s[i]] = map_s.get(s[i] , 0) + 1

            while self.hasElements(map_s , map_t) : 
                if i - start + 1 < minimum_window_length : 
                    minimum_window_length = i - start + 1
                    ans_string = s[start : i+1]
                map_s[s[start]] = map_s.get(s[start] , 0) - 1
                if map_s[s[start]] == 0 : 
                    del map_s[s[start]]
                start+=1

        return ans_string
 
        
    def hasElements(self , map1 : {str , int} , map2 : {str : int}) -> bool : 
        for u in map2 : 
            if u not in map1 or map1[u]<map2[u] : 
                return False
        return True