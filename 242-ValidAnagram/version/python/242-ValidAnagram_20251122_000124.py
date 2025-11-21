# Last updated: 11/22/2025, 12:01:24 AM
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False

        first_word = defaultdict(int)
        for i in range(len(s)) : 
            first_word[s[i]] +=1
        
        second_word = defaultdict(int)
        for i in range(len(t)) : 
            second_word[t[i]] +=1
        
        if len(first_word) != len(second_word) : 
            return False
        
        for key in first_word.keys(): 
            if key not in second_word or second_word[key] != first_word[key] : 
                return False
        
        return True