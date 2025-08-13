# Last updated: 8/13/2025, 8:20:32 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict_s = {}
        my_dict_t = {}

        for i in range (0,len(s)):
            my_dict_s[s[i]] = my_dict_s.get(s[i] , 0) + 1
        
        for i in range (0,len(t)):
            my_dict_t[t[i]] = my_dict_t.get(t[i], 0) + 1

        if len(my_dict_s)!=len(my_dict_t) :
            return False
        
        for key in my_dict_s.keys() :
            if my_dict_s.get(key) != my_dict_t.get(key):
                return False
        
        return True