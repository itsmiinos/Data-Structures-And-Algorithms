class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) : 
            return ""

        map_t = {}

        for i in range(len(t)) : 
            map_t[t[i]] = map_t.get(t[i] , 0) + 1
        
        start = 0
        window = {}
        min_string = ""
        min_length = float('inf')

        for index in range(len(s)) : 

            window[s[index]] = window.get(s[index] , 0) + 1

            while self.hasElements(window , map_t) :
                if (index - start + 1) < min_length : 
                    min_length = index - start + 1
                    min_string = s[start : index+1]
                
                window[s[start]] = window.get(s[start] , 0) - 1
                if window[s[start]] == 0 :
                    del window[s[start]]
                start+=1
            
        return min_string
        

    
    def hasElements(self , map1 : {str : int} , map2 : {str , int}) -> bool :
        for key in map2 : 
            if key not in map1 or map1[key] < map2[key] : 
                return False
        return True